%define commit b619262405d19ae8831fd91b2b29bd85c5b23d84

Name: scoutfish
Version: 20170627.9.gitb619262
Release: alt1

Summary: Chess query engine for PGN databases

License: GPL-3.0-or-later
Group: Games/Boards
Url: https://github.com/pychess/scoutfish

# Source-url: https://github.com/pychess/scoutfish/archive/%commit.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: nlohmann-json-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: python3 python3-module-pexpect}}

%description
Scoutfish lets you run powerful and flexible queries on very big chess
databases (PGN files) with very high speed. It builds an index (.scout
file) from a PGN file and answers JSON queries (sub-FEN, material,
side to move, result, move sequences and so on) with JSON results.

Scoutfish is based on the Stockfish chess engine and is used by PyChess
for database queries.

%prep
%setup
# use system nlohmann-json instead of the bundled copy
rm -v src/json.hpp
sed -i 's|#include "json.hpp"|#include <nlohmann/json.hpp>|' src/scout.cpp
# do not force -m32/-m64 (unknown on non-x86 compilers)
sed -i 's|-m$(bits)||g' src/Makefile
sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/python3|' src/*.py

%build
# generic targets only, no -march=native
%ifarch x86_64
%global sfarch x86-64
%else
%if "%_lib" == "lib64"
%global sfarch general-64
%else
%global sfarch general-32
%endif
%endif

%make_build -C src build ARCH=%sfarch \
	EXTRACXXFLAGS="%optflags" \
	EXTRALDFLAGS="%optflags"

%install
install -D -m 755 -p src/%name %buildroot%_bindir/%name

%check
cd src
# ParserTestCase is a known failing upstream testcase (pychess issue #1550:
# game offsets after extra newlines); pychess compensates for it, and the
# fix (upstream PR #7) changes the .scout format, so it is not applied.
python3 test.py TestSuite

%files
%doc Copying.txt README.md
%_bindir/%name

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 20170627.9.gitb619262-alt1
- initial build for Sisyphus
