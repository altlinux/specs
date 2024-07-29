%define pypi_name PyWavefront
%define oname pywavefront

%def_without check

Name: python3-module-%oname
Version: 1.3.3
Release: alt1

Summary: Python library for importing Wavefront .obj files

Url: https://github.com/pywavefront/PyWavefront
License: BSD-3-Clause
Group: Development/Python3

BuildArch: noarch

# Source-url:https://github.com/pywavefront/PyWavefront/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
PyWavefront reads Wavefront 3D object files (something.obj, something.obj.gz and something.mtl) and generates interleaved
vertex data for each material ready for rendering.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri Jul 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.3.3-alt1
- initial build for ALT Sisyphus

