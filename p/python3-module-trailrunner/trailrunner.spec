%define _unpackaged_files_terminate_build 1
%define pypi_name trailrunner

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1
Summary: Run things on paths
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/trailrunner
Vcs: https://github.com/omnilib/trailrunner
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter attribution
%pyproject_builddeps_metadata_extra dev
%endif

%description
trailrunner is a simple library for walking paths on the filesystem, and
executing functions for each file found. trailrunner obeys project level
.gitignore files, and runs functions on a process pool for increased
performance. trailrunner is designed for use by linting, formatting, and other
developer tools that need to find and operate on all files in project in a
predictable fashion with a minimal API.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
%pyproject_run -- python3 -m %pypi_name.tests -v

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.2.1 -> 1.4.0.

* Wed Nov 16 2022 Michael Shigorin <mike@altlinux.org> 1.2.1-alt2
- BR: python3(pathspec) is requisite for %%build, not just %%check.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.3 -> 1.2.1.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
