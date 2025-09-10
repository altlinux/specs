%define _unpackaged_files_terminate_build 1
%define pypi_name libvcs
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.36.0
Release: alt1

Summary: Lite, typed, pythonic utilities for git, svn, mercurial, etc
License: MIT
Group: Development/Python3
Url: https://libvcs.git-pull.com/
Vcs: https://github.com/vcs-python/libvcs
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: git
BuildRequires: subversion
BuildRequires: subversion-server-common
BuildRequires: mercurial
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

# don't add requires found in the pytest plugin to the requirement list
%add_findreq_skiplist %python3_sitelibdir/%module_name/pytest_plugin.py

%description
libvcs is a lite, typed, pythonic tool box for detection and parsing of
URLs, commanding, and syncing with git, hg, and svn. Powers vcspull.

Key Features:
- URL Detection and Parsing: Validate and parse Git, Mercurial, and
  Subversion URLs.
- Command Abstraction: Interact with VCS systems through a Python API.
- Repository Synchronization: Clone and update repositories locally
  via Python API.
- py.test fixtures: Create temporary local repositories and working
  copies for testing for unit tests.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup testing
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
# Tests are hardcoded to load source files of this module from the src/. You
# can see that in the pyproject.toml file in the pytest settings section.
PYTHONPATH=src python3 -m pytest
ENDTESTS

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.36.0-alt1
- Initial build for ALT Sisyphus.

