%define _unpackaged_files_terminate_build 1
%define pypi_name three-merge
%define mod_name three_merge

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: Simple Python library to perform a 3-way merge between strings
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/three-merge/
Vcs: https://github.com/spyder-ide/three-merge

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
Simple Python library to perform a 3-way merge between strings,
based on diff-match-patch. This library performs merges at a character
level, as opposed to most VCS systems, which opt for a line-based
approach.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md CHANGELOG.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-%version.dist-info/

%changelog
* Sat Oct 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Built for ALT Sisyphus.

