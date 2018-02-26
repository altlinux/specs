%define php5_extension xcache

Name: php5-xcache
Version: 1.3.0
Release: alt11

Summary: XCache is a fast, stable  PHP opcode cacher
License: GPL
Group: System/Servers

Url: http://xcache.lighttpd.net/
Source0: %name-%version.tar
Source1: %php5_extension.ini
Source2: %php5_extension-params.ini
Packager: Maxim Ivanov <redbaron@altlinux.org>

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires(pre): rpm-build-php5 
BuildRequires(pre): rpm-build-php5 = %php5_version
BuildRequires: php5-devel = %php5_version
Prereq: php5-libs = %php5_version

%description
XCache is a open-source opcode cacher, which means that it accelerates 
the performance of PHP on servers. It optimizes performance by removing the 
compilation time of PHP scripts by caching the compiled state of PHP scripts 
into the shm (RAM) and uses the compiled version straight from the RAM. This 
will increase the rate of page generation time by up to 5 times as it also
optimizes many other aspects of php scripts and reduce serverload. 

%prep
%setup 

%build
%add_optflags -fPIC
pushd %php5_extension
phpize
%configure \
--enable-xcache 
%php5_make
popd

%install
pushd %php5_extension
%php5_make_install
mkdir -p %buildroot/%_cachedir/%php5_extension
install -D -m644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params
popd

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%_cachedir/%php5_extension

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 1.3.0-alt11
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.3.0-alt10
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1.3.0-alt9
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1.3.0-alt8
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1.3.0-alt7
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt6
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt5
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt4
- Rebuild with php5-5.3.3.20100722-alt1

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt3
- Rebuild with php5-5.2.14.20100721-alt1

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2
- Rebuild with php5-5.2.13.20100205-alt1

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- new version
- fixed requires

* Sun Aug 02 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2.2-alt2
- Fix build deps

* Tue Jul 14 2009 Ivanov Maxim <redbaron@altlinux.org> 1.2.2-alt1
- Initial build for ALTLinux

