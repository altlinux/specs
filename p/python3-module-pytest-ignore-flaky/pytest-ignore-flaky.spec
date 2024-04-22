%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-ignore-flaky
%define mod_name pytest_ignore_flaky

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1
Summary: Ignore failures from flaky tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-ignore-flaky
Vcs: https://github.com/schettino72/pytest-ignore-flaky
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
Ignore failures from flaky tests (pytest plugin).

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.2.0 -> 2.2.1.

* Mon Apr 08 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.0.0 -> 2.2.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
