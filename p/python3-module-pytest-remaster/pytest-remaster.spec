%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-remaster
%define mod_name pytest_remaster

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1
Summary: Pytest plugin for golden master (characterisation) testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-remaster
Vcs: https://github.com/Pierre-Sassoulas/pytest-remaster
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
# filtered by default, required by tests/demo_pylint/test_functional.py
BuildRequires: python3-module-pylint
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 02 2026 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1
- Initial build for sisyphus.
