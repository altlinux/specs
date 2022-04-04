%define modulename boltons

Name: python3-module-boltons
Version: 21.0.0
Release: alt1

Summary: When they're not builtins, they're boltons.

Url: https://github.com/boltons/boltons/
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/b/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

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
%python3_prune

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 21.0.0-alt1
- new version 21.0.0 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 20.2.1-alt1
- new version 20.2.1 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 20.0.0-alt1
- new version 20.0.0 (with rpmrb script)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 19.1.0-alt1
- initial build for ALT Sisyphus
