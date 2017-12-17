# Spec file for mod_perl2 module for Apache 2.0 server

%define real_name    mod_perl
%define module_name  perl

Name:    apache2-mod_perl
Version: 2.0.10
Release: alt4.1

Summary: An embedded Perl interpreter for the Apache2 Web server
Summary(ru_RU.UTF-8): Встроенный интерпретатор Perl для веб-сервера Apache2

License: Apache License v. 2.0
Group:   System/Servers

URL:     http://perl.apache.org/
Source:  mod_perl-%version.tar
Source1: perl.load
Source2: perl.conf
Source3: perl.start

Source4: Apache-Test-1.39.tar
Source5: Apache-SizeLimit-0.96.tar
Source6: Apache-Reload-0.13.tar
Source7: docs-2.0.tar


Patch1: mod_perl-2.0.5-lfs.patch
Patch2: mod_perl-2.0.7-alt-disable_prctl_set_name.patch
Patch4: mod_perl-2.0.10-test_config.patch

Provides: mod_perl = %version

Requires(pre): apache2 >= %apache2_version
BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires: apache2-httpd-prefork
BuildRequires: %apache2_apr_buildreq
BuildRequires: libgdbm-devel

# Automatically added by buildreq on Wed Oct 26 2011 (-bi)
BuildRequires: apache2-devel libexpat-devel perl-BSD-Resource perl-CGI perl-DBD-DBM perl-Devel-Symdump perl-LWP-Protocol-https perl-Linux-Pid perl-Math-BigInt perl-Test-Pod perl-pod perl-podlators perl-threads

# syntax check failes
%add_findreq_skiplist */Apache/Test*
%add_findreq_skiplist */Apache2/SizeLimit.pm
%add_findreq_skiplist */Apache/SizeLimit.pm
%add_findreq_skiplist */ModPerl/Code.pm
%add_findreq_skiplist */ModPerl/RegistryLoader.pm

# extra dependencies
%add_findreq_skiplist */Apache2/compat.pm
%add_findreq_skiplist */ModPerl/CScan.pm

%define common_desc Mod_perl  incorporates a  Perl  interpreter into the  Apache web\
server, so that the  Apache web server can directly execute Perl\
code.

%define common_desc_ru Mod_perl  встраивает интерпретатор Perl в веб-сервер Apache,\
позволяя веб серверу непосредственно исполнять код на Perl.


%description
%common_desc

Mod_perl provides an object-oriented Perl interface for Apache's
C language API and allows to manage Apache,  respond to requests
for web pages  and much more.  The end result  is a quicker  CGI
script  turnaround process,  since no external  Perl interpreter
has to be started.

Install  mod_perl if you're installing the Apache web server and
you'd like for it to directly incorporate a Perl interpreter.

%description -l ru_RU.UTF-8
%common_desc_ru

Mod_perl предоставляет объектно-ориентированный интерфейс на
Perl к внутреннему API Apache  и позволяет управлять Apache,
отвечать на запросы  веб-страниц и многое другое. В конечном
итоге,  использование mod_perl позволяет ускорить выполнение
CGI-скриптов, так как исключает необходимость в вызовах 
внешнего интерпретатора Perl.

Mod_perl может быть полезен,  если Вы установили  веб-сервер
Apache и Вам нужна интегрированная поддержка Perl в нём.

%package devel
Summary: Files needed for building XS modules that use mod_perl
Summary(ru_RU.UTF-8): Файлы для сборки модулей Perl, использующих mod_perl
Group:    Development/C
Requires: %name = %version-%release
Requires: apache2-devel

%description devel
%common_desc

This package contains the files needed for building XS modules
that use mod_perl.

%description devel -l ru_RU.UTF-8
%common_desc_ru

Данный пакет содержит файлы, необходимые для разработки
XS-модулей на Perl, использующих mod_perl.


%package doc
Summary: mod_perl2 Apache module documentation
Summary(ru_RU.UTF-8): Документация к модулю Apache mod_perl2
Group:     Documentation
Requires:  %name = %version
BuildArch: noarch

%description doc
%common_desc

This package contains the documentation for mod_perl2 Apache2
module.

%description doc -l ru_RU.UTF-8
%common_desc_ru

Данный пакет содержит документацию к модулю mod_perl2.


%prep
%setup -n mod_perl-%version
%patch1 -p1
%patch2
%patch4 -p1

# Complete installation with separate projects
tar xvf %SOURCE4
tar xvf %SOURCE5
tar xvf %SOURCE6
tar xvf %SOURCE7

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

# Hardcode module versions to make perl.prov happy (ALT#29362)
VERSION=`grep 'our $VERSION = "' lib/mod_perl2.pm | sed -e 's#[^"]*"##' -e 's#".*##'`
sed -e "s#VERSION = do { require mod_perl2; \$mod_perl2::VERSION }#VERSION = \"$VERSION\"#" -i xs/ModPerl/Const/Const.pm
sed -e "s#VERSION = do { require mod_perl2; \$mod_perl2::VERSION }#VERSION = \"$VERSION\"#" -i xs/Apache2/Const/Const.pm


%ifdef __BTE
rm -f -- t/response/TestAPR/finfo.pm t/apr-ext/finfo.t t/lib/TestAPRlib/finfo.pm
%endif

#setup apache modules path for test config
sed 's,@apache2_moduledir@,%apache2_moduledir,' -i t/conf/extra.conf.in

%build
%perl_vendor_build MP_APXS=%apache2_apxs MP_APR_CONFIG=%apache2_apr_config \
    MP_CCOPTS=-fgnu89-inline

%install
%perl_vendor_install

# Install the config file
install -d -m 755 -- %buildroot%apache2_mods_available
install -d -m 755 -- %buildroot%apache2_mods_start

install -p -m 644 -- %SOURCE1 %buildroot%apache2_mods_available/%module_name.load
install -p -m 644 -- %SOURCE2 %buildroot%apache2_mods_available/%module_name.conf
sed -i 's,@a_libexecdir@,%apache2_libexecdir,g' %buildroot%apache2_mods_available/%module_name.load
install -p -m 644 -- %SOURCE3 %buildroot%apache2_mods_start/100-%module_name.conf

# Install missed modules from install script
install -p -m 644 -- xs/tables/current/APR/FunctionTable.pm      %buildroot%perl_vendor_archlib/APR/FunctionTable.pm
install -p -m 644 -- xs/tables/current/Apache2/ConstantsTable.pm %buildroot%perl_vendor_archlib/Apache2/ConstantsTable.pm
install -p -m 644 -- xs/tables/current/Apache2/FunctionTable.pm  %buildroot%perl_vendor_archlib/Apache2/FunctionTable.pm
install -p -m 644 -- xs/tables/current/Apache2/StructureTable.pm %buildroot%perl_vendor_archlib/Apache2/StructureTable.pm
install -p -m 644 -- xs/tables/current/ModPerl/FunctionTable.pm  %buildroot%perl_vendor_archlib/ModPerl/FunctionTable.pm

%files
%doc Changes README
%doc --no-dereference LICENSE

%config(noreplace) %apache2_mods_available/%module_name.conf
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf

%apache2_libexecdir/%real_name.so

%perl_vendor_archlib/mod_perl2.pm
%perl_vendor_autolib/mod_perl2
%perl_vendor_archlib/Apache
%perl_vendor_archlib/Apache2
%perl_vendor_autolib/Apache2
%perl_vendor_archlib/APR*
%perl_vendor_autolib/APR
%perl_vendor_archlib/ModPerl
%perl_vendor_autolib/ModPerl

# mod_perl-1.x
%exclude %perl_vendor_archlib/Apache/SizeLimit.pm

# Install helpers - do not need them
%exclude %perl_vendor_archlib/Bundle*
%exclude %perl_vendor_archlib/MyTest*


%exclude %perl_vendor_archlib/Apache/Test*
%exclude %perl_vendor_archlib/Apache2/Build.pm
%exclude %perl_vendor_archlib/Apache2/BuildConfig.pm
%exclude %perl_vendor_archlib/Apache2/ParseSource.pm
%exclude %perl_vendor_archlib/ModPerl/BuildMM.pm
%exclude %perl_vendor_archlib/ModPerl/BuildOptions.pm
%exclude %perl_vendor_archlib/ModPerl/CScan.pm
%exclude %perl_vendor_archlib/ModPerl/Code.pm
%exclude %perl_vendor_archlib/ModPerl/Config.pm
%exclude %perl_vendor_archlib/ModPerl/FunctionMap.pm
%exclude %perl_vendor_archlib/ModPerl/MM.pm
%exclude %perl_vendor_archlib/ModPerl/Manifest.pm
%exclude %perl_vendor_archlib/ModPerl/MapUtil.pm
%exclude %perl_vendor_archlib/ModPerl/ParseSource.pm
%exclude %perl_vendor_archlib/ModPerl/StructureMap.pm
%exclude %perl_vendor_archlib/ModPerl/TestReport.pm
%exclude %perl_vendor_archlib/ModPerl/TestRun.pm
%exclude %perl_vendor_archlib/ModPerl/TypeMap.pm
%exclude %perl_vendor_archlib/ModPerl/WrapXS.pm

%files devel
%doc SVN-MOVE BRANCHING README-SVN RELEASE STATUS
%_bindir/mp2bug

%apache2_includedir/mod_perl.h
%apache2_includedir/modperl_*.h

%dir %perl_vendor_archlib/Apache
%dir %perl_vendor_archlib/Apache2
%dir %perl_vendor_archlib/ModPerl

%perl_vendor_archlib/Apache/Test*
%perl_vendor_archlib/Apache2/Build.pm
%perl_vendor_archlib/Apache2/BuildConfig.pm
%perl_vendor_archlib/Apache2/ParseSource.pm
%perl_vendor_archlib/ModPerl/BuildMM.pm
%perl_vendor_archlib/ModPerl/BuildOptions.pm
%perl_vendor_archlib/ModPerl/CScan.pm
%perl_vendor_archlib/ModPerl/Code.pm
%perl_vendor_archlib/ModPerl/Config.pm
%perl_vendor_archlib/ModPerl/FunctionMap.pm
%perl_vendor_archlib/ModPerl/MM.pm
%perl_vendor_archlib/ModPerl/Manifest.pm
%perl_vendor_archlib/ModPerl/MapUtil.pm
%perl_vendor_archlib/ModPerl/ParseSource.pm
%perl_vendor_archlib/ModPerl/StructureMap.pm
%perl_vendor_archlib/ModPerl/TestReport.pm
%perl_vendor_archlib/ModPerl/TestRun.pm
%perl_vendor_archlib/ModPerl/TypeMap.pm
%perl_vendor_archlib/ModPerl/WrapXS.pm

%files doc
%doc docs/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt4.1
- rebuild with new perl 5.26.1

* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.0.10-alt4
- Fix tests for Apache >= 2.4.25 stricter HTTP RFC 7230 complience

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt3.1
- rebuild with new perl 5.24.1

* Thu Jun 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.10-alt3
- Updating to the current 2.0.10-dev to support Perl 5.22.x (Closes: #32179)

* Thu May 12 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.10-alt2
- fix tests httpd.conf
- revert test switching off

* Mon Apr 11 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.10-alt1
- rebuild with apache-2.4

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt0.1.1
- rebuild with new perl 5.22.0

* Mon Nov 23 2015 Vladimir Lettiev <crux@altlinux.ru> 2.0.10-alt0.1
- 2.0.10-dev
- fixed build with Perl 5.22: patch from RT#101962
- fixed build with GCC 5
- updated Apache::Test 1.39, Apache::Reload 0.13
- enabled tests

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt3.1
- rebuild with new perl 5.20.1

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.8-alt3
- Hardcode modules versions to make perl.prov happy (Closes: #29362)
- Switch to use httpd2.filetrigger

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0.8-alt2
- built for perl 5.18
- temporary disabled tests (sporadic failures in BTE on i586)

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.8-alt1
- New version 2.0.8

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.7-alt5
- build fixed

* Sun Dec 16 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.7-alt4
- Disable changing the proctitle (Closes: #26892, #27924)

* Wed Nov 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.7-alt3
- Excluding Apache/SizeLimit.pm (Closes: #26508)
- Make use of triggers to restart Apache2 on package install/uninstall

* Mon Nov 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.7-alt2
- Fix build with HTTP::Headers 6.001
- Restoring proper translation and formatting in spec file

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.0.7-alt1
- 2.0.5 -> 2.0.7
- built for perl-5.16
- dropped patches mod_perl-2.0.5-sv_dup.patch, mod_perl-2.0.5-lwp6.patch
  (applied upstream)

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 2.0.5-alt2
- exclude Apache/SizeLimit.pm, due to conflict with mod_perl-1.x (ALT#26508)

* Fri Oct 14 2011 Alexey Tourbin <at@altlinux.ru> 2.0.5-alt1
- 2.0.4 -> 2.0.5
- built for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.4-alt1.1
- rebuilt with perl 5.12

* Thu Dec 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.4-alt1
- New version 2.0.4

* Sun Nov 23 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt5.9
- Adding Provides for mod_perl (#13307)
- Rebuild with perl-5.8.8-alt16

* Sat Apr 28 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt5
- Disabling tests for release versions
- Fix Apache2 test configuration

* Fri Mar 30 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt4
- Fix for CVE-2007-1349: mod_perl "path_info" DoS Vulnerability
- Switch to the new Apache2 configuration scheme
- Disabling tests required mod_dir
- Disabling tests while building on ALT Linux BTE
- Spec file cleanup

* Fri Mar 23 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt3
- Adding patch to build with perl-5.8.8-alt7, thanks Alexey Tourbin (at@)
- Disable ulimit setting during tests to build in hasher

* Mon Mar 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt2
- Build for Apache 2.2

* Mon Jan 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.3-alt1
- Initial build for ALT Linux Sisyphus

* Tue Oct 17 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.2-alt0
- Initial build
