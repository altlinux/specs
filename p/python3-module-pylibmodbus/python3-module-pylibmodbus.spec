%define pypi_name pylibmodbus
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.6.2
Release: alt1

Summary: Python wrapper for libmodbus

Url: https://pypi.org/project/pylibmodbus
License: Apache-2.0
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: pkgconfig(libmodbus)
BuildRequires: libffi-devel

%description
Python Interface for libmodbus written with CFFI.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Dec 16 2025 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Sisyphus

