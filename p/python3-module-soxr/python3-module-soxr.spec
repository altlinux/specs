%define pypi_name soxr
%ifarch ppc64le
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Python-SoXR is a Python wrapper of libsoxr
Group: Development/Python3
License: LGPL-2.1-or-later
Url: https://pypi.org/project/soxr

Vcs: https://github.com/dofuuz/python-soxr.git
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: cmake gcc-c++
BuildRequires: python3(setuptools_scm) python3(wheel)
BuildRequires: python3(scikit_build_core) python3(nanobind)
BuildRequires: libsoxr-devel libnumpy-py3-devel python3-module-numpy
%{?_enable_check:BuildRequires: /proc python3-module-pytest}

%description
This package provides Python 3 wrappers for the SoX Resampler library.

%prep
%setup -n %pypi_name-%version
rm -rf libsoxr

cat <<_EOF_ >> pyproject.toml
[tool.scikit-build.cmake.define]
USE_SYSTEM_LIBSOXR={env="USE_SYSTEM_LIBSOXR", default="OFF"}
_EOF_

%build
export USE_SYSTEM_LIBSOXR=ON
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%_bindir/py.test3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Mon Aug 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Jul 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Tue Aug 15 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6
- ported to %%pyproject* macros

* Sat Apr 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Fri Mar 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Wed Feb 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- first build for Sisyphus

