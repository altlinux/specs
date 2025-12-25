%define oname mautrix

Name: python3-module-%oname
Version: 0.21.0
Release: alt1

Summary: A Python 3 asyncio Matrix framework

Url: https://github.com/mautrix/python
License: MPL-2.0
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
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Dec 01 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.21.0-alt1
- Init build for ALT Sisyphus

