Name: pam_python
Version: 1.0.8
Release: alt2

Summary: A Pluggable Authentication Module that runs the Python interpreter

# https://github.com/Ralnoc/pam-python
URL: https://sourceforge.net/projects/pam-python
License: AGPLv3
Group: System/Base

# Source-url: https://prdownloads.sourceforge.net/pam-python/pam-python-%version-1/pam-python-%version.tar.gz
Source: %name-%version.tar

Patch: pam_python.python3.patch

BuildRequires: libpam-devel >= 0.76
BuildRequires: rpm-build-python3 python3-dev python3-module-setuptools

# doc
BuildRequires: python3-module-sphinx

# for test
BuildRequires: python3-module-PAM

%description
pam_python is a PAM module that runs the Python interpreter
and so allows PAM modules to be written in Python.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation and examples for
%summary

See also https://github.com/privacyidea/pam_python as example.

%prep
%setup
%patch -p1
subst "s|-Werror||" src/Makefile
subst "s|sphinx-build|sphinx-build-3|" doc/Makefile

%build
cd src && %python3_build_debug ; cd -
# hack
p=$(echo src/build/lib*)
cp $p/pam_python*.so $p/pam_python.so
%make_build LIBDIR=%_pam_modules_dir

%install
%makeinstall_std LIBDIR=%_pam_modules_dir

%files
%_pam_modules_dir/pam_python.so
#_mandir/man5/*
%doc README.txt

%files doc
%doc %_docdir/%name/

%changelog
* Sun Mar 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt2
- add missed python3-dev

* Fri Mar 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- new version 1.0.8 (with rpmrb script)
- switch to python3

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- initial build for ALT Sisyphus
