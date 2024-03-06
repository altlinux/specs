%define _unpackaged_files_terminate_build 1
%define pypi_name assertpy
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1
Release: alt1
Summary: Simple assertion library for unit testing in python with a fluent API
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/assertpy
Vcs: https://github.com/assertpy/assertpy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
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
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 05 2024 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- Initial build for Sisyphus.
