%define _unpackaged_files_terminate_build 1
%define pypi_name geomdl
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.3.1
Release: alt1
Summary: Object-oriented B-Spline and NURBS evaluation library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/geomdl
VCS: https://github.com/orbingol/NURBS-Python.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

%if_with check
# optional dependencies (visualization)
BuildRequires: python3(numpy)
BuildRequires: python3(matplotlib)
# plotly is not packaged yet
# BuildRequires: python3(plotly)

BuildRequires: python3(pytest)
%endif

# plotly is not packaged yet, but it's optional
%filter_from_requires /python3(plotly\(\..*\)\?)/d

%description
%pypi_name is a pure Python, object-oriented B-Spline and NURBS library. It is
compatible with Python versions 2.7.x, 3.4.x and later.

%prep
%setup
%autopatch -p1

%build
%pyproject_build --backend-config-settings='{"--build-option": ["--use-cython"]}'

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- Initial build for Sisyphus.
