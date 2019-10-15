%define modulename boltons

Name: python3-module-boltons
Version: 19.1.0
Release: alt1

Summary: When they're not builtins, they're boltons.

Url: https://github.com/boltons/boltons/
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/b/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
Functionality that should be in the standard library. Like builtins, but Boltons.

Otherwise known as, "everyone's util.py", but cleaned up and tested.

Contains over 230 BSD-licensed utility types and functions that can be used as a package or independently.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/%modulename/tests/

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 19.1.0-alt1
- initial build for ALT Sisyphus
