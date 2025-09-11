%define pypi_name pymadcad
%define oname madcad

Name: python3-module-%oname
Version: 0.19.0
Release: alt1.1

Summary: Simple yet powerful CAD (Computer Aided Design) library, written with Python

Url: https://github.com/jimy-byerley/pymadcad
License: LGPL-3.0 AND GPL-3.0
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

Requires: python3(pywavefront) python3(plyfile) python3(stl)

%description
%summary

%prep
%setup

# Force cythonize
rm -v madcad/core.c

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 11 2025 Grigory Ustinov <grenka@altlinux.org> 0.19.0-alt1.1
- Fix building with python3.13.

* Sat Jun 28 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)

* Mon May 26 2025 Stanislav Levin <slev@altlinux.org> 0.16.0-alt1.1
- NMU: fixed FTBFS (PyGLM 2.8.2-alt1).

* Fri Jul 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.16.0-alt1
- initial build for ALT Sisyphus
