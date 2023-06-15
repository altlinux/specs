%define _unpackaged_files_terminate_build 1
%define pypi_name Deprecated
%define mod_name deprecated

%def_with check

Name: python3-module-%mod_name
Version: 1.2.14
Release: alt1
Summary: Decorators to deprecate old python classes, functions or methods
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Deprecated/
Vcs: https://github.com/tantale/deprecated
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter 'bump2version$'
%pyproject_builddeps_metadata_extra dev
%endif

%description
Python @deprecated decorator to deprecate old python classes, functions or
methods.

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
%doc README.md CHANGELOG.rst
%python3_sitelibdir/deprecated/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Jun 14 2023 Stanislav Levin <slev@altlinux.org> 1.2.14-alt1
- 1.2.13 -> 1.2.14.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.2.13-alt1
- 1.2.12 -> 1.2.13.

* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 1.2.12-alt1
- Initial build for Sisyphus.
