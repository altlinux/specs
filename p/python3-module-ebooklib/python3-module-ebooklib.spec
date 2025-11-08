%define oname ebooklib

Name: python3-module-ebooklib
Version: 0.20
Release: alt1

Summary: A versatile Python library for EPUB2/EPUB3 manipulation and processing

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
EbookLib is a Python library for managing EPUB2/EPUB3. It's capable of reading and writing EPUB files programmatically.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Fri Nov 07 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.20-alt1
- new version (0.20) with rpmgs script

* Wed May 29 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.18-alt1
- initial build for ALT Sisyphus

