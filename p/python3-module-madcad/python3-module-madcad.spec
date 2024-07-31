%define pypi_name pymadcad
%define oname madcad

Name: python3-module-%oname
Version: 0.16.0
Release: alt1

Summary: Simple yet powerful CAD (Computer Aided Design) library, written with Python

Url: https://github.com/jimy-byerley/pymadcad
License: LGPL-3.0 AND GPL-3.0
Group: Development/Python3

%filter_from_requires /python3(glm)/d

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Requires: python3(PyGLM) python3(pywavefront) python3(plyfile) python3(stl)

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
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.16.0-alt1
- initial build for ALT Sisyphus
