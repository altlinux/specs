%define pypi_name aggdraw

Name: python3-module-aggdraw
Version: 1.4.1
Release: alt1

Summary: High quality drawing interface for PIL

License: MIT
Group: Development/Python3
URL: https://github.com/pytroll/aggdraw
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-packaging
BuildRequires: gcc-c++ libfreetype-devel

%description
The aggdraw module implements the basic WCK 2D Drawing Interface on top
of the AGG library. This is a high quality graphics engine with
anti-aliasing and alpha compositing.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aggdraw*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Sisyphus

