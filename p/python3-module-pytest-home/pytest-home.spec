%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-home
%define mod_name pytest_home

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1
Summary: Pytest fixtures for working with home directories
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-home
Vcs: https://github.com/jaraco/pytest-home
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary

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
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.1 -> 0.6.0.

* Wed Feb 14 2024 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus.
