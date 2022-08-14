%define _unpackaged_files_terminate_build 1
%define pypi_name aiosqlite

%def_with check

Name: python3-module-%pypi_name
Version: 0.17.0
Release: alt1.gitde63727c

Summary: asyncio bridge to the standard sqlite3 module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiosqlite

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(flit)
BuildRequires: python3(sqlite3) 

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
aiosqlite provides a friendly, async interface to sqlite databases.

It replicates the standard sqlite3 module, but with async versions of all
the standard connection and cursor methods, plus context managers for
automatically closing connections and cursors. It can also be used in
the traditional, procedural manner. aiosqlite also replicates most of
the advanced features of sqlite3

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# remove tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests

%check
cat << EOF > tox.ini
[testenv]
commands = python3 -m aiosqlite.tests
EOF
%tox_check_pyproject

%files
%doc README.rst LICENSE CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt1.gitde63727c
- initial build for Sisyphus

