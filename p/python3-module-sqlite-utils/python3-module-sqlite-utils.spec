%define _unpackaged_files_terminate_build 1
%define pypi_name sqlite-utils
%define pypi_nname sqlite-utils
%define mod_name sqlite_utils

%def_with check

Name: python3-module-%pypi_nname
Version: 3.39
Release: alt1

Summary: Python CLI utility and library for manipulating SQLite databases
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sqlite-utils/
Vcs: https://github.com/simonw/sqlite-utils

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
Requires: python3-modules-sqlite3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-modules-sqlite3
%endif

%description
%summary.

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
%_bindir/sqlite-utils
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 3.39-alt1
- Updated to 3.39.

* Sun Nov 02 2025 Grigory Ustinov <grenka@altlinux.org> 3.38-alt2
- Fixed FTBFS.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 3.38-alt1
- Built for ALT Sisyphus.

