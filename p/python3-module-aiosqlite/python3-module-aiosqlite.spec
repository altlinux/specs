%define _unpackaged_files_terminate_build 1
%define pypi_name aiosqlite

%def_with check

Name: python3-module-%pypi_name
Version: 0.19.0
Release: alt1

Summary: asyncio bridge to the standard sqlite3 module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiosqlite
Vcs: https://github.com/omnilib/aiosqlite
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check

BuildRequires: python3(sqlite3)
BuildRequires: python3(pytest)
%endif

%description
aiosqlite provides a friendly, async interface to sqlite databases.

It replicates the standard sqlite3 module, but with async versions of all
the standard connection and cursor methods, plus context managers for
automatically closing connections and cursors. It can also be used in
the traditional, procedural manner. aiosqlite also replicates most of
the advanced features of sqlite3

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync check metadata
%endif

%build
%pyproject_build

%install
%pyproject_install

# remove tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests

%check
%pyproject_run_unittest aiosqlite.tests

%files
%doc README.rst CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.19.0-alt1
- New version.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.18.0-alt1
- New version.

* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt1.gitde63727c
- initial build for Sisyphus

