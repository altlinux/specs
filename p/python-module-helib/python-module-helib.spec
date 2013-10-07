%define modulename helib

Name: python-module-helib
Version: 0.1
Release: alt1

Summary: Helib: Useful python library

Group: Development/Python
License: GPLv3+
Url: https://github.com/mdevaev/helib

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mdevaev/helib.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %modulename

BuildRequires: python-dev python-module-distribute

%description
Helib: Useful python library

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
* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
