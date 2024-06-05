%define oname EbookLib

Name: python3-module-ebooklib
Version: 0.18
Release: alt1

Summary: A jazzy skin for the Django Admin-Interface

Url: https://github.com/aerkalov/ebooklib
License: AGPL-3.0-or-later
Group: Development/Python3

# Source-url: %__pypi_url %oname
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
%python3_sitelibdir/*

%changelog
* Wed May 29 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.18-alt1
- initial build for ALT Sisyphus

