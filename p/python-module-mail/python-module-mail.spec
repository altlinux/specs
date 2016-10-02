Name: python-module-mail
Version: 2.1.0
Release: alt1

Summary: Simple wrapper over Python's email package for common operations, and a mail pipe

Url: http://jimmyg.org/work/code/mail/index.html
License: GNU AGPLv3
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.python.org/packages/1d/74/0a90cb0fe1e9536d83fc3c4e06c9559687813f214b57a3ba3e707365de7f/Mail-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%description
Simple wrapper over Python's email package for common operations.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir_noarch/mail
%python_sitelibdir_noarch/*.egg-info/

%changelog
* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus
