%define _unpackaged_files_terminate_build 1
%define pypi_name packaging-legacy
%define mod_name packaging_legacy

%def_with check

Name: python3-module-%pypi_name
Version: 23.0.post0
Release: alt1
Summary: Core utilities for legacy Python packages
License: Apache-2.0 or BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/packaging-legacy
Vcs: https://github.com/di/packaging_legacy
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
This library provides support for "legacy" Python Packaging functionality
removed from https://github.com/pypa/packaging.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
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
* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 23.0.post0-alt1
- Initial build for Sisyphus.
