%define php5_extension ctpp

Name: php5-ctpp
Version: 2.6.0
Release: alt7

Summary: PHP ctpp2 template engine driver
License: BSD
Group: System/Servers

Source0: %name-%version.tar
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

BuildRequires: gcc-c++ libctpp-devel

BuildRequires(pre): rpm-build-php5
BuildRequires: rpm-build-php5 = %php5_version
BuildRequires: php5-devel = %php5_version
BuildRequires: libctpp-devel
Prereq: php5-libs = %php5_version

%description
This package provides an interface for communicating with the ctppDB
database in PHP.

%prep
%setup

%build
%add_optflags -fPIC
phpize
%configure
sed -i "s!-Wl,-rpath,%_libdir!!" Makefile
sed -i "s!-Wl,-rpath,\${libdir}!!" Makefile
%php5_make

%install
%php5_make_install
mkdir -p %buildroot/%_cachedir/%php5_extension
install -pDm644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -pDm644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%_cachedir/%php5_extension
%doc hello.tmpl README

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 2.6.0-alt7
- Rebuild with php5-5.3.10.20120202-alt1

* Sat Jan 14 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt6.1
- fix build (remove -rpath ${libdir})

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 2.6.0-alt6
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 2.6.0-alt5
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 2.6.0-alt4
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 2.6.0-alt3
- Rebuild with php5-5.3.5.20110105-alt1

* Sun Feb 06 2011 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt2
- rebuild with new ctpp

* Wed Feb 02 2011 Denis Smirnov <mithraen@altlinux.ru> 2.6.0-alt1
- first build for Sisyphus

