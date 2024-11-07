%define _unpackaged_files_terminate_build 1
%define pypi_name nbmake
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.4
Release: alt1
Summary: Pytest plugin for testing notebooks
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nbmake
Vcs: https://github.com/treebeardtech/nbmake
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# test_when_parallel_passing_nbs_then_ok fails on girar x86_64 with 32 workers
export PYTEST_XDIST_AUTO_NUM_WORKERS=2
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus.
