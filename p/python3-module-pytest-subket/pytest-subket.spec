%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-subket
# it's a fork of pytest-socket, but pytest-socket provides a module
# (pytest_socket.py)
%define mod_name pytest_socket

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
Summary: Pytest Plugin to disable socket calls during tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-subket
Vcs: https://github.com/ichard26/pytest-subket
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# conflicts with python3-module-pytest-socket
# it's a fork of pytest-socket,
# pytest-socket provides a module pytest_socket.py,
# pytest-subket provides a package pytest_socket,
# autoreq/autoprov doesn't support such a difference and think this is the same
%filter_from_provides /python3(pytest_socket\(\..*\)\?)/d
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
A plugin to use with Pytest to disable or restrict socket calls during tests to
ensure network calls are prevented.

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
%pyproject_run_pytest -vra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name.pth
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 31 2025 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
