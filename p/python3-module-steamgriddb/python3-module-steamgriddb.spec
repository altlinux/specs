%define oname steamgriddb
%define pypi_name python-steamgriddb

Name: python3-module-%oname
Version: 1.0.5
Release: alt1

Summary: A Python API wrapper for SteamGridDB.com

Url: https://github.com/ZebcoWeb/python-steamgriddb
License: MIT
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/steamgrid
%python3_sitelibdir/%{pyproject_distinfo python_steamgriddb}

%changelog
* Tue Aug 06 2024 Mikhail Tergoev <fidel@altlinux.org> 1.0.5-alt1
- initial build for ALT Sisyphus

