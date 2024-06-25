%define _unpackaged_files_terminate_build 1
%define pypi_name seedir
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: Creating, editing and reading folder tree diagrams
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/seedir
Vcs: https://github.com/earnestt1234/seedir
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
%_bindir/seedir
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 25 2024 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.2 -> 0.5.0.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.
