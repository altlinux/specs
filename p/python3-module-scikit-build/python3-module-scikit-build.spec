%define modname scikit-build
%define pypi_name scikit_build
%define _name skbuild

%def_disable check

Name: python3-module-%modname
Version: 0.17.6
Release: alt1.1

Summary: Improved build system generator for CPython C/C++/Fortran/Cython extensions
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/scikit-build/scikit-build.git
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz
Patch: scikit_build-0.17.6-up-no-distutils-cmake.patch

BuildArch: noarch

Requires: cmake make ninja-build gcc-c++
# skbuild/_compat/tomllib.py
%if "%__python3_version" <= "3.11"
Requires: python3(tomli)
%else
Requires: python3(tomllib)
%endif

# for python w/o distutils
%filter_from_requires /python3(distutils.*)/d
Requires: python3(setuptools._distutils)

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
BuildRequires: python3(hatchling) python3(hatch-fancy-pypi-readme) python3(hatch-vcs)
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
%summary
Better support is available for additional compilers, build systems,
cross compilation, and locating dependencies and determining their build
requirements.

The scikit-build package is fundamentally just glue between the
setuptools Python module and CMake.

%prep
%setup -n %pypi_name-%version
%patch -p1

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
%doc README* CHANGES*


%changelog
* Fri Oct 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.6-alt1.1
- prepared for python w/o distutils

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.6-alt1
- 0.17.6

* Thu May 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4

* Mon Apr 24 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Tue Apr 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1.1
- explicitly required python3(tomli) if %%__python_version <= 3.11

* Thu Apr 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Thu Feb 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.16.7-alt1
- 0.16.7

* Sat Dec 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.16.4-alt1
- 0.16.4

* Thu Dec 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Wed Nov 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.16.2-alt1
- first build for Sisyphus


