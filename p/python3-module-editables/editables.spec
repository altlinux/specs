%define _unpackaged_files_terminate_build 1
%define pypi_name editables

%def_with check

Name: python3-module-%pypi_name
Version: 0.4
Release: alt1
Summary: Editable installations
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/editables
Vcs: https://github.com/pfmoore/editables
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
A Python library for creating "editable wheels".
This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode". In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3 -> 0.4.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2 -> 0.3.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
