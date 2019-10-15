%define modulename pem

Name: python3-module-pem
Version: 19.2.0
Release: alt1

Summary: Easy PEM file parsing in Python

Url: https://github.com/hynek/pem
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
pem is an MIT-licensed Python module for parsing and splitting of PEM files,
i.e. Base64 encoded DER keys and certificates.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 19.2.0-alt1
- initial build for ALT Sisyphus
