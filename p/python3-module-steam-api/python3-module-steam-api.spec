%define oname steam-api
%define pypi_name python_steam_api

Name: python3-module-%oname
Version: 2.0.3
Release: alt2

Summary: This library providing of steam-api

Url: https://github.com/deivit24/python-steam-api
License: MIT
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
%python3_sitelibdir/steam_web_api
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 13 2024 Mikhail Tergoev <fidel@altlinux.org> 2.0.3-alt2
- fixed build for p11

* Tue Aug 06 2024 Mikhail Tergoev <fidel@altlinux.org> 2.0.3-alt1
- initial build for ALT Sisyphus
