Name: pam_python
Version: 1.0.7
Release: alt1

Summary: A Pluggable Authentication Module that runs the Python interpreter

# https://github.com/Ralnoc/pam-python
URL: https://sourceforge.net/projects/pam-python
License: AGPLv3
Group: System/Base

# Source-url: https://prdownloads.sourceforge.net/pam-python/pam-python-%version-1/pam-python-%version.tar.gz
Source: %name-%version.tar

BuildRequires: libpam-devel
BuildRequires: rpm-build-python python-module-setuptools python-module-sphinx

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
#patch -p1

%build
# TODO: change with python_build
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
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- initial build for ALT Sisyphus
