%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-server
%define mod_name devpi_server

%def_with check

Name: python3-module-%pypi_name
Version: 6.20.3
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
# not packaged yet
%add_pyproject_deps_build_filter setuptools-changelog-shortener
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
cd server
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
cd server
%pyproject_build

%install
cd server
%pyproject_install

# tests are packaged on purpose because they are required by other devpi
# packages. Don't want to bother with splitting entry points. Tests don't
# have third party dependencies (don't enable autoreq for python)

%check
cd server
%pyproject_run_pytest -ra

%files
%_bindir/devpi-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/pytest_devpi_server/
%python3_sitelibdir/test_devpi_server/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 02 2026 Stanislav Levin <slev@altlinux.org> 6.20.3-alt1
- 6.20.1 -> 6.20.3

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 6.20.1-alt1
- 6.19.3 -> 6.20.1.

* Tue Apr 14 2026 Stanislav Levin <slev@altlinux.org> 6.19.3-alt1
- 6.19.2 -> 6.19.3.

* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 6.19.2-alt1
- 6.19.1 -> 6.19.2.

* Tue Feb 10 2026 Stanislav Levin <slev@altlinux.org> 6.19.1-alt1
- 6.19.0 -> 6.19.1.

* Mon Feb 09 2026 Stanislav Levin <slev@altlinux.org> 6.19.0-alt1
- 6.17.0 -> 6.19.0.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 6.17.0-alt1
- 6.16.0 -> 6.17.0.

* Thu Jun 26 2025 Stanislav Levin <slev@altlinux.org> 6.16.0-alt1
- 6.15.0 -> 6.16.0.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 6.15.0-alt1
- 6.14.0 -> 6.15.0.

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
