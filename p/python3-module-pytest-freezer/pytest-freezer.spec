%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-freezer
%define mod_name pytest_freezer

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.8
Release: alt1
Summary: Pytest plugin providing a fixture interface for spulec/freezegun
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-freezer
Vcs: https://github.com/pytest-dev/pytest-freezer
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary.

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 0.4.8-alt1
- 0.4.6 -> 0.4.8.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 0.4.6-alt1
- Initial build for Sisyphus.
