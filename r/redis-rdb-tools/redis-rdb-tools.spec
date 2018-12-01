Name: redis-rdb-tools
Version: 0.1.13
Release: alt1

Summary: Parse Redis dump.rdb files, Analyze Memory, and Export Data to JSON

Url: https://rdbtools.com
License: MIT License
Group: Databases

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sripathikrishnan/redis-rdb-tools/archive/rdbtools-%version.tar.gz
Source: %name-%version.tar

Provides: rdbtools = %EVR

# (highly recommended to speed up parsing)
Requires: python-module-lzf

BuildRequires: python-modules-json

# for ./run_tests
BuildRequires: python-module-redis-py python-modules-unittest

BuildArch: noarch

%description
Parse Redis dump.rdb files, Analyze Memory, and Export Data to JSON
Rdbtools is a parser for Redis' dump.rdb files.

The parser generates events similar to an xml sax parser,
and is very efficient memory wise.

In addition, rdbtools provides utilities to:
* Generate a Memory Report of your data across all databases and keys
* Convert dump files to JSON
* Compare two dump files using standard diff tools

%prep
%setup

%build
%python_build

%install
%python_install

%check
./run_tests

%files
%doc README.md
%_bindir/rdb
%_bindir/redis-memory-for-key
%_bindir/redis-profiler
%python_sitelibdir/*

%changelog
* Sat Dec 01 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1.13-alt1
- initial build for ALT Linux Sisyphus
