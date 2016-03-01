%define module_name tinyec

Name: python-module-tinyec
Version: 0.3.1
Release: alt1

Summary: A tiny library to perform arithmetic operations on elliptic curves in pure python

Group: Development/Python
License: GPL3
Url: https://pypi.python.org/pypi/tinyec

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.python.org/packages/source/t/tinyec/tinyec-%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-distribute

%description
A tiny library to perform arithmetic operations on elliptic curves in pure python. No dependencies.

**This is not a library suitable for production.**
It is useful for security professionals to understand the inner workings of EC,
and be able to play with pre-defined curves.


%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%module_name/
%python_sitelibdir/%module_name-*egg-info

%changelog
* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Sisyphus

