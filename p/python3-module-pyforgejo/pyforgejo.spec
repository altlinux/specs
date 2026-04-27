%global _unpackaged_files_terminate_build 1
%define pypi_name pyforgejo
%def_without check

Name: python3-module-pyforgejo
Version: 2.0.7
Release: alt1
Summary: A Python client library for accessing the Forgejo API
Group: Development/Python3
License: MIT
BuildArch: noarch
Url: https://pypi.org/project/pyforgejo/
VCS: https://github.com/harabat/pyforgejo
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Python client for the Forgejo REST API.
Supports typed requests/responses for Forgejo entities and operations.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Upstream test suite is fully integration-based (requires live Forgejo API,
# network access, and credentials via BASE_URL/PYTEST_API_KEY), so tests are
# disabled for reproducible offline RPM builds.

%files
%doc README.md LICENSE
%python3_sitelibdir/pyforgejo/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 21 2026 Matvey Pyanov <sen@altlinux.org> 2.0.7-alt1
- First build for ALT Linux.
