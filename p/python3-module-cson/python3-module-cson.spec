%define pypi_name cson
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.8
Release: alt1

Summary: A parser for Coffeescript Object Notation (CSON)

Url: https://pypi.org/project/cson
License: Apache-2.0
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A python parser for the Coffeescript Object Notation (CSON).

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
* Sun Mar 17 2024 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Sisyphus

