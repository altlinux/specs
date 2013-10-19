%define modulename ulib

Name: python-module-%modulename
Version: 0.4
Release: alt1

Summary: ulib: Useful python library

Group: Development/Python
License: GPLv3+
Url: https://pypi.python.org/pypi/ulib

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mdevaev/ulib.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %modulename

BuildRequires: python-dev python-module-distribute

%description
Useful python library.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Sat Oct 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus

* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
