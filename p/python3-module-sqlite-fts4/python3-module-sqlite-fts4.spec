%define _unpackaged_files_terminate_build 1
%define pypi_name sqlite-fts4
%define pypi_nname sqlite-fts4
%define mod_name sqlite_fts4

%def_with check

Name: python3-module-%pypi_nname
Version: 1.0.3
Release: alt1

Summary: Custom Python functions for working with SQLite FTS4
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sqlite-fts4/
Vcs: https://github.com/simonw/sqlite-fts4

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-modules-sqlite3
%endif

%description
Custom SQLite functions written in Python for ranking documents indexed
using the FTS4 extension.

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
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- Built for ALT Sisyphus.

