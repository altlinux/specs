%define _unpackaged_files_terminate_build 1
%define pypi_name time-machine
%define mod_name time_machine

%def_with check

Name: python3-module-%pypi_name
Version: 2.9.0
Release: alt1
Summary: Travel through time in your tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/time-machine
Vcs: https://github.com/adamchainz/time-machine
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
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/requirements.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus.
