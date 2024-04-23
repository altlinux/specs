%define _unpackaged_files_terminate_build 1
%define pypi_name repo-review
%define mod_name repo_review

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.6
Release: alt1
Summary: Framework that can run checks on repos
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/repo-review
Vcs: https://github.com/scientific-python/repo-review
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# sp-repo-review is not packaged yet
%add_pyproject_deps_check_filter sp-repo-review
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra cli
%endif

%description
This is a framework for building checks designed to check to see if a repository
follows guidelines. By itself, it does nothing - it requires at least one plugin
to be installed.

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
%doc README.*
%_bindir/repo-review
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 0.10.6-alt1
- 0.10.0 -> 0.10.6.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 0.10.0-alt2
- Fixed FTBFS (hatchling 1.23.0).

* Thu Sep 28 2023 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus.
