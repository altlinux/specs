%define _unpackaged_files_terminate_build 1

%define pypi_name gast
%define mod_name %pypi_name

%def_with check

Name: python3-module-gast
Version: 0.5.5
Release: alt1
Summary: Python AST that abstracts the underlying Python version
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/gast/
Vcs: https://github.com/serge-sans-paille/gast
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 26 2024 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1
- 0.5.3 -> 0.5.5.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.5.3-alt1.1
- NMU: added missing build dependency on setuptools.

* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- first build for Sisyphus, based on specfile from Fedora
