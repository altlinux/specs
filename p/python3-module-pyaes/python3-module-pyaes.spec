%define modulename pyaes

Name: python3-module-pyaes
Version: 1.6.1
Release: alt1

Summary: Pure-Python Implementation of the AES block-cipher and common modes of operation

Url: https://github.com/ricmoo/pyaes
License: MIT
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
A pure-Python implementation of the AES (FIPS-197)
block-cipher algorithm and common modes of operation (CBC, CFB, CTR, ECB,
OFB) with no dependencies beyond standard Python libraries. See README.md
for API reference and details.

%prep
%setup -n pyaes-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- new version 1.6.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- initial build for ALT Sisyphus
