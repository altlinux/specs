%define oname desktop-parser

Name: python3-module-%oname
Version: 0.1.1
Release: alt1

Summary: This is a parser for the .desktop file format.

Url: https://github.com/Atrophaneura/desktop-parser
License: GPL-3.0
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry-core)

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
%python3_sitelibdir/desktop_parser
%python3_sitelibdir/%{pyproject_distinfo desktop_parser}


%changelog
* Tue Aug 06 2024 Mikhail Tergoev <fidel@altlinux.org> 0.1.1-alt1
- initial build for ALT Sisyphus
