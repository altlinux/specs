%define oname lottie

Name: python3-module-%oname
Version: 0.7.2
Release: alt1

Summary: A Python framework to work with Lottie files and Telegram animated stickers

Url: https://pypi.org/project/lottie/
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
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}
%_bindir/*.py

%changelog
* Tue Dec 02 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.7.2-alt1
- Init build for ALT Sisyphus
