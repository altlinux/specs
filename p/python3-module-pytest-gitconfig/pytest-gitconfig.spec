%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-gitconfig
%define mod_name pytest_gitconfig

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1
Summary: Provide a Git config sandbox for testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-gitconfig
Vcs: https://github.com/noirbizarre/pytest-gitconfig
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged in sisyphus
%add_pyproject_deps_check_filter pytest-mypy-testing
%add_pyproject_deps_check_filter tox-pdm
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pdm test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 07 2025 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
