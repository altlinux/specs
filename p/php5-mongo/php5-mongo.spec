%define php5_extension mongo

Name: php5-mongo
Version: 1.1.0
Release: alt7

Summary: PHP MongoDB driver
License: Apache license
Group: System/Servers

Source0: %name-%version.tar
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires(pre): rpm-build-php5
BuildRequires: rpm-build-php5 = %php5_version
BuildRequires: php5-devel = %php5_version
Prereq: php5-libs = %php5_version

%description
This package provides an interface for communicating with the MongoDB
database in PHP.

%prep
%setup

%build
%add_optflags -fPIC
phpize
%configure
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
%doc php README.md
# doc/ belongs to examples subpackage, sample php code
#doc doc/

%post
%php5_extension_postin

%preun
%php5_extension_preun

# TODO:
# - conditional eloader/encoder build?
# - add/separate admin stuff (see also spec attached to #19996)

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 1.1.0-alt7
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.1.0-alt6
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1.1.0-alt5
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1.1.0-alt4
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1.1.0-alt3
- Rebuild with php5-5.3.5.20110105-alt1

* Tue Jan 04 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1.0-alt2
- fix description (Closes: #24851)

* Sun Jan 02 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1.0-alt1
- first build for Sisyphus

