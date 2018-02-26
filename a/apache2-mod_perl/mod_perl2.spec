Name: apache2-mod_perl
Version: 2.0.5
Release: alt2

Summary: An embedded Perl interpreter for the Apache2 Web server
Summary(ru_RU.UTF-8): Встроенный интерпретатор пёрла для веб-сёрвера Апаче2
License: Apache License v. 2.0
Group: System/Servers

URL: http://perl.apache.org/
Source: http://perl.apache.org/dist/mod_perl-%version.tar.gz
Source1: perl.load
Source2: perl.conf
Source3: perl.start

Patch0: mod_perl-2.0.2-multilib.patch
Patch1: mod_perl-2.0.5-sv_dup.patch
Patch2: mod_perl-2.0.5-lwp6.patch
Patch3: mod_perl-2.0.5-lfs.patch

Provides: mod_perl = %version

Requires(pre): apache2 >= %apache2_version
BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires: apache2-httpd-prefork
BuildRequires: %apache2_apr_buildreq

# Automatically added by buildreq on Wed Oct 26 2011 (-bi)
BuildRequires: apache2-devel libexpat-devel perl-BSD-Resource perl-CGI perl-DBD-DBM perl-Devel-Symdump perl-LWP-Protocol-https perl-Linux-Pid perl-Math-BigInt perl-Test-Pod perl-pod perl-podlators perl-threads

# syntax check failes
%add_findreq_skiplist */Apache/Test*
%add_findreq_skiplist */Apache2/SizeLimit.pm
%add_findreq_skiplist */ModPerl/Code.pm
%add_findreq_skiplist */ModPerl/RegistryLoader.pm

# extra dependencies
%add_findreq_skiplist */Apache2/compat.pm
%add_findreq_skiplist */ModPerl/CScan.pm

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.

Mod_perl provides an object-oriented Perl interface for Apache's C
language API and allows to manage Apache, respond to requests for web
pages and much more. The end result is a quicker CGI script turnaround
process, since no external Perl interpreter has to be started.

Install mod_perl if you're installing the Apache web server and you'd
like for it to directly incorporate a Perl interpreter.

%description -l ru_RU.UTF-8
Мод_пёрл встраивает интерпретатор пёрла в веб-сёрвер Апаче, позволяя
веб-сёрверу непосредственно исполнять код на пёрле.

Мод_пёрл предоставляет объектно-ориентированный интерфейс на пёрле к
внутреннему АПИ Апаче и позволяет управлять Апаче, отвечать на запросы
веб-страниц и многое другое. В конечном итоге, использование мод_пёрла
позволяет ускорить выполнение ЦГИ-скриптов, так как исключает необходимость
в вызовах внешнего интерпретатора пёрла.

Мод_пёрл может быть полезен, если Вы установили веб-сёрвер Апаче и Вам нужна
интегрированная поддержка пёрла в нём.

%package devel
Summary: Files needed for building XS modules that use mod_perl
Summary(ru_RU.UTF-8): Файлы для сборки модулей пёрла, использующих мод_пёрл
Group: Development/C
Requires: %name = %version-%release
Requires: apache2-devel

%description devel
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.

This package contains the files needed for building XS modules that
use mod_perl.

%description devel -l ru_RU.UTF-8
Мод_пёрл встраивает интерпретатор пёрла в веб-сёрвер Апаче, позволяя
веб-сёрверу непосредственно исполнять код на пёрле.

Данный пакет содержит файлы, необходимые для разработки XC-модулей на пёрле,
использующих мод_пёрл.

%package doc
Summary: Mod_perl2 Apache module documentation
Summary(ru_RU.UTF-8): Документация к модулю Апаче мод_прёл
Group: Documentation
Requires: %name = %version
BuildArch: noarch

%description doc
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.

This package contains the documentation for mod_perl Apache2 module.

%description doc -l ru_RU.UTF-8
Мод_пёрл встраивает интерпретатор пёрла в веб-сёрвер Апаче, позволяя
веб-сёрверу непосредственно исполнять код на пёрле.

Данный пакет содержит документацию к мод_пёрлу.

%prep
%setup -n mod_perl-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%perl_vendor_build MP_APXS=%apache2_apxs MP_APR_CONFIG=%apache2_apr_config

%install
%perl_vendor_install

# Install the config file
install -d -m 755 %buildroot%apache2_mods_available
install -d -m 755 %buildroot%apache2_mods_start

install -p -m 644 %SOURCE1 %buildroot%apache2_mods_available/perl.load
install -p -m 644 %SOURCE2 %buildroot%apache2_mods_available/perl.conf
sed -i 's,@a_libexecdir@,%apache2_libexecdir,g' %buildroot%apache2_mods_available/perl.load
install -p -m 644 %SOURCE3 %buildroot%apache2_mods_start/100-perl.conf

# Install missed modules from install script
install -p -m 644 xs/tables/current/APR/FunctionTable.pm      %buildroot%perl_vendor_archlib/APR/FunctionTable.pm
install -p -m 644 xs/tables/current/Apache2/ConstantsTable.pm %buildroot%perl_vendor_archlib/Apache2/ConstantsTable.pm
install -p -m 644 xs/tables/current/Apache2/FunctionTable.pm  %buildroot%perl_vendor_archlib/Apache2/FunctionTable.pm
install -p -m 644 xs/tables/current/Apache2/StructureTable.pm %buildroot%perl_vendor_archlib/Apache2/StructureTable.pm
install -p -m 644 xs/tables/current/ModPerl/FunctionTable.pm  %buildroot%perl_vendor_archlib/ModPerl/FunctionTable.pm

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/perl.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To use mod_perl check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 mod_perl module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with 'perl=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/perl.load ] && %apache2_sbindir/a2dismod perl 2>&1 >/dev/null ||:
fi

%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete mod_perl uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi

%files
%doc Changes README

%config(noreplace) %apache2_mods_available/perl.conf
%config            %apache2_mods_available/perl.load
%config            %apache2_mods_start/100-perl.conf

%apache2_libexecdir/mod_perl.so

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

%exclude %perl_vendor_archlib/Bundle

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
