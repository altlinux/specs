%define _unpackaged_files_terminate_build 1
%define pypi_name tox-console-scripts
%define mod_name tox_console_scripts

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt2
Summary: Tox plugin for installation of console scripts for system site packages
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-console-scripts/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
It's possible to use system site packages within Python virtual environment,
but there is no way to install console or gui scripts into such environment.

With the help of this plugin the corresponding scripts will be automatically
generated for system site packages calculated as dependencies of current
environment.

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 12 2024 Stanislav Levin <slev@altlinux.org> 0.3.2-alt2
- Fixed FTBFS.

* Fri Jun 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1
- 0.2 -> 0.3.2.

* Wed Mar 10 2021 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- 0.1 -> 0.2.

* Wed Dec 30 2020 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build.
