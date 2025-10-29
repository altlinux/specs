%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-process
%define mod_name devpi_process

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1
Summary: Programmatic API to create and use a devpi server process
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-process
Vcs: https://github.com/tox-dev/devpi-process
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
Allows you to create devpi server process with indexes, and upload artifacts to
that programmatically.

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
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 29 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.2 -> 1.1.0.

* Sun May 25 2025 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Fixed extra name used for pulling tests dependencies.

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
