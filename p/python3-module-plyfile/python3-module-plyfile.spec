%define oname plyfile

Name: python3-module-plyfile
Version: 1.0.3
Release: alt1

Summary: NumPy-based text/binary PLY file reader/writer for Python

Url: https://github.com/dranjan/python-plyfile
License: GPL-3.0-only
Group: Development/Python3

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-pdm-pep517

%description
Welcome to the plyfile Python module, which provides a simple facility for reading and writing ASCII and binary PLY files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname.py
%python3_sitelibdir/%{pyproject_distinfo %oname}
%python3_sitelibdir/__pycache__/%oname.cpython*

%changelog
* Fri Jul 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.0.3-alt1
- initial build for ALT Sisyphus

