%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-socket
%define mod_name pytest_socket

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1
Summary: Pytest Plugin to disable socket calls during tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-socket
Vcs: https://github.com/miketheman/pytest-socket
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
A plugin to use with Pytest to disable or restrict socket calls during tests to
ensure network calls are prevented.

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
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Feb 19 2024 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
