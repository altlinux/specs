%define pypi_name pi-heif
%define mod_name pi_heif

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Python interface for libheif library

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/bigcat88/pillow_heif

# Source-url: %__pypi_url %mod_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-devel
BuildRequires: libheif-devel

%description
Python interface for libheif library.
pi-heif is a light version of Pillow-Heif with more permissive license
for binary wheels. It includes only HEIF decoder and does not support
save operations.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_pi_heif*.so
%python3_sitelibdir/%mod_name-%version.dist-info/

%changelog
* Thu Mar 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Sisyphus

