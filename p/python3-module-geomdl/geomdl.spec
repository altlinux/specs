%define _unpackaged_files_terminate_build 1
%define pypi_name geomdl
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.3.1
Release: alt2
Summary: Object-oriented B-Spline and NURBS evaluation library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/geomdl
VCS: https://github.com/orbingol/NURBS-Python.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# plotly is not packaged yet, but it's optional
%filter_from_requires /python3(plotly\(\..*\)\?)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
# not listed
BuildRequires: python3-module-cython
%if_with check
%pyproject_builddeps_metadata
# not listed
BuildRequires: python3-module-pytest
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-numpy
%endif

%description
%pypi_name is a pure Python, object-oriented B-Spline and NURBS library. It is
compatible with Python versions 2.7.x, 3.4.x and later.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build --backend-config-settings='{"--build-option": ["--use-cython"]}'

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 5.3.1-alt2
- Added compatibility with numpy 1.25.0.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- Initial build for Sisyphus.
