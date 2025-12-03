%define _unpackaged_files_terminate_build 1
%define pypi_name pyprobables
%define mod_name probables

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.2
Release: alt1
Summary: Probabilistic data structures in python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyprobables
Vcs: https://github.com/barrust/pyprobables
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
pyprobables is a pure-python library for probabilistic data structures. The goal
is to provide the developer with a pure-python implementation of common
probabilistic data-structures to use in their work.

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
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2.

* Tue Jun 17 2025 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
