%define _unpackaged_files_terminate_build 1
%define pypi_name geographiclib
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.0
Release: alt1
Summary: The geodesic routines from GeographicLib
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/geographiclib/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

%description
This is a library to solve geodesic problems on an ellipsoid model of the earth.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%mod_name/test/

%check
%pyproject_run_unittest -v %mod_name.test.test_geodesic

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 11 2024 Stanislav Levin <slev@altlinux.org> 2.0-alt1
- 1.50 -> 2.0.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.50-alt1
- Initial build for Sisyphus

