%define oname django-grappelli

Name: python3-module-django-grappelli
Version: 4.0.1
Release: alt1

Summary: A jazzy skin for the Django Admin-Interface

Url: https://github.com/sehmaschine/django-grappelli
License: BSD-3-Clause
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
* Tue May 28 2024 Ivan Mazhukin <vanomj@altlinux.org> 4.0.1-alt1
- Initial build for Alt Sisyphus
