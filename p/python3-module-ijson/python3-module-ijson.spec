%def_without check

%define oname ijson
Name: python3-module-ijson
Version: 3.1.4
Release: alt1

Summary: Iterative JSON parser with standard Python iterator interfaces

Url: https://github.com/ICRAR/ijson
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools

BuildRequires: libyajl-devel

%description
Ijson is an iterative JSON parser with standard Python iterator interfaces.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Tue Jun 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- initial build for ALT Sisyphus

