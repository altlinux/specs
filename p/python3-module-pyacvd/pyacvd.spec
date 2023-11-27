%define _unpackaged_files_terminate_build 1
# Non-system Cython libraries cannot link to python3.11
# with Cython == 0.29 during build
%set_verify_elf_method skip

%define oname pyacvd

Name: python3-module-%oname
Version: 0.2.10
Release: alt1

Summary: Python implementation of surface mesh resampling algorithm ACVD.
License: MIT
Group: Development/Python3
URL: https://github.com/pyvista/pyacvd
VCS: https://github.com/pyvista/pyacvd.git

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pyvista
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-scipy

%description
This module takes a surface mesh and returns a uniformly meshed
surface using voronoi clustering. This approach is loosely based on
research by S. Valette, and J. M. Chassery in ACVD.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# Install tests
mkdir -p %buildroot%python3_sitelibdir/%oname/tests
cp -far tests/*.py %buildroot%python3_sitelibdir/%oname/tests

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname/*
%python3_sitelibdir/%oname-%version.dist-info/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Nov 23 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0.2.10-alt1
- Updated version, dependencies.

* Wed Oct 18 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0.2.9-alt1
- Initial build for ALT.

