%define _unpackaged_files_terminate_build 1
%define pypi_name validate-pyproject

%def_with check

Name: python3-module-%pypi_name
Version: 0.14
Release: alt1
Summary: Validation pyproject.toml files using JSON Schema
License: MPL-2.0 and MIT and BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/validate-pyproject
VCS: https://github.com/abravalheri/validate-pyproject.git
BuildArch: noarch
Source: %name-%version.tar
Source1: pyproject_deps.json
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_metadata_extra testing
%endif

%description
Validation library and CLI tool for checking on 'pyproject.toml' files using
JSON Schema.

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
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.rst
%_bindir/validate-pyproject
%python3_sitelibdir/validate_pyproject/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 28 2023 Stanislav Levin <slev@altlinux.org> 0.14-alt1
- 0.13 -> 0.14.

* Fri May 19 2023 Stanislav Levin <slev@altlinux.org> 0.13-alt1
- 0.12.2 -> 0.13.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 0.12.2-alt1
- 0.12.1 -> 0.12.2.

* Fri Mar 10 2023 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.12 -> 0.12.1.

* Thu Jan 26 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.10.1 -> 0.12.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9 -> 0.10.1.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.7.1 -> 0.9.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
