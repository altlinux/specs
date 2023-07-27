%define _unpackaged_files_terminate_build 1
%define pypi_name interegular
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt1
Summary: A regex intersection checker
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/interegular
Vcs: https://github.com/MegaIng/interegular
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
A library to check a subset of python regexes for intersections.

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus.
