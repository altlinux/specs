%define modname scikit-build
%define pypi_name scikit_build
%define _name skbuild

%def_disable check

Name: python3-module-%modname
Version: 0.16.3
Release: alt1

Summary: Improved build system generator for CPython C/C++/Fortran/Cython extensions
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/scikit-build/scikit-build.git
Source: http://pypi.io/packages/source/s/%pypi_name/%modname-%version.tar.gz

BuildArch: noarch

Requires: cmake make ninja-build gcc-c++

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
BuildRequires: python3-module-setuptools python3-module-setuptools_scm
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
%summary
Better support is available for additional compilers, build systems,
cross compilation, and locating dependencies and determining their build
requirements.

The scikit-build package is fundamentally just glue between the
setuptools Python module and CMake.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/%_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* HISTORY* CHANGES*


%changelog
* Thu Dec 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Wed Nov 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.16.2-alt1
- first build for Sisyphus


