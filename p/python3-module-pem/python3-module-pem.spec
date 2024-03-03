%define modulename pem

Name: python3-module-pem
Version: 23.1.0
Release: alt1

Summary: Easy PEM file parsing in Python

Url: https://github.com/hynek/pem
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
BuildRequires: python3-module-hatch-fancy-pypi-readme

BuildArch: noarch

%description
pem is an MIT-licensed Python module for parsing and splitting of PEM files,
i.e. Base64 encoded DER keys and certificates.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.dist-info/

%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 23.1.0-alt1
- new version 23.1.0
- switch to pyproject_build

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 21.2.0-alt1
- new version 21.2.0 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 20.1.0-alt1
- new version 20.1.0 (with rpmrb script)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 19.2.0-alt1
- initial build for ALT Sisyphus
