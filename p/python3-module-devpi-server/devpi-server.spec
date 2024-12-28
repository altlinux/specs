%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-server
%define mod_name devpi_server

%def_with check

Name: python3-module-%pypi_name
Version: 6.14.0
Release: alt1
Summary: Reliable private and pypi.org caching server
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-server
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# subpackaged
Requires: python3-modules-sqlite3
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-github-actions-annotate-failures
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
%endif

%description
Server for private package indexes and PyPI caching.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

# tests are packaged on purpose because they are required by other devpi
# packages. Don't want to bother with splitting entry points. Tests don't
# have third party dependencies (don't enable autoreq for python)

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%_bindir/devpi-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/pytest_devpi_server/
%python3_sitelibdir/test_devpi_server/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
