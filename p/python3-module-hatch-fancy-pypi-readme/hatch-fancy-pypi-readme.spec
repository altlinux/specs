%define _unpackaged_files_terminate_build 1

%define oname hatch-fancy-pypi-readme
%define modname hatch_fancy_pypi_readme

%def_with check

Name: python3-module-%oname
Version: 23.1.0
Release: alt1
Summary: Fancy PyPI READMEs with Hatch
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-fancy-pypi-readme/
VCS: https://github.com/hynek/hatch-fancy-pypi-readme.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %oname
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
hatch-fancy-pypi-readme is a Hatch metadata plugin for everyone who cares
about the first impression of their project's PyPI landing page.

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
%pyproject_run_pytest -ra -Wignore

%files
%_bindir/%oname
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon May 22 2023 Stanislav Levin <slev@altlinux.org> 23.1.0-alt1
- 22.8.0 -> 23.1.0.

* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 22.8.0-alt1
- 22.3.0 -> 22.8.0.

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 22.3.0-alt1
- Initial build for Sisyphus
