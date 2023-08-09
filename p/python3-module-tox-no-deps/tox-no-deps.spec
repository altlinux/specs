%define _unpackaged_files_terminate_build 1

%define pypi_name tox-no-deps
%define mod_name tox_no_deps

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt2
Summary: Tox plugin for skipping the installation of all deps and extras
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-no-deps/
Vcs: https://github.com/stanislavlevin/tox-no-deps
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
This plugin skips the installation of all deps and extras of all the Tox
environments. The dependencies of tested package if any are not touched.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PIP_NO_INDEX=YES
%pyproject_run_pytest -ra -Wignore tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (Python 3.11).
- Modernized packaging.

* Tue Jun 14 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- 0.1 -> 0.2.0.

* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
