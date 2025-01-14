%define _unpackaged_files_terminate_build 1
%define pypi_name pathable

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.4
Release: alt1
Summary: Object-oriented paths
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pathable
Vcs: https://github.com/p1c2u/pathable
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
Object-oriented paths.

Key features:
- Traverse resources like paths
- Access resources on demand with separate accessor layer

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 13 2025 Stanislav Levin <slev@altlinux.org> 0.4.4-alt1
- 0.4.3 -> 0.4.4.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus.
