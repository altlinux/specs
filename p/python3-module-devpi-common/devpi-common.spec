%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-common
%define mod_name devpi_common

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.4
Release: alt1
Summary: This package contains utility functions used by devpi-server and devpi-client
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-common
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter setuptools-changelog-shortener
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-github-actions-annotate-failures
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
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

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
* Thu May 30 2024 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus.
