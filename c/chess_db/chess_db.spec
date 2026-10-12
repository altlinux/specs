Name: chess_db
Version: 20170627
Release: alt1

Summary: Chess database opening tree indexer for PGN files

License: GPL-3.0-only
Group: Games/Boards
URL: https://github.com/pychess/chess_db

# Source-url: https://github.com/pychess/chess_db/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

%if_disabled check
%else
BuildRequires: python3-module-pexpect
%endif

%description
chess_db indexes PGN files into polyglot opening books with the standard
moves and weights, extended with Win/Loss/Draw statistics and game offset
information. It is used by PyChess to show the opening tree of a database.

The upstream binary "parser" is installed as chess_db.

%prep
%setup
# drop -m32/-m64: unsupported by gcc on non-x86 architectures
sed -i 's|-m$(bits)||g' parser/Makefile
# do not overlink with unneeded libraries
sed -i 's|-Wl,--no-as-needed||' parser/Makefile
sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/python3|' parser/*.py

%build
%make_build -C parser build \
	ARCH=general-$(getconf LONG_BIT) \
	EXTRACXXFLAGS="%optflags"

%install
install -D -m0755 parser/parser %buildroot%_bindir/%name

%check
cd parser
python3 test.py | tee test.log
grep -q '^games ' test.log
! grep -q FAIL test.log

%files
%doc README.md parser/chess_db.py
%_bindir/%name

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 20170627-alt1
- initial build for Sisyphus
