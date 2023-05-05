%define _unpackaged_files_terminate_build 1
%define pypi_name asttokens
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1
Summary: Annotate AST trees with source code positions
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/asttokens
Vcs: https://github.com/gristlabs/asttokens
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
The ``asttokens`` module annotates Python abstract syntax trees (ASTs) with the
positions of tokens and text in the source code that generated them.

It makes it possible for tools that work with logical AST nodes to find the
particular text that resulted in those nodes, for example for automated
refactoring or highlighting.

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
%pyproject_run_pytest -ra

%files
%doc README*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 26 2023 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.0.5 -> 2.2.1.

* Thu Oct 21 2021 Ildar Mulyukov <ildar@altlinux.ru> 2.0.5-alt1
- 1st build for Sisyphus
