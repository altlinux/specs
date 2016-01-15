%set_verify_elf_method unresolved=strict

Name: gnustep-Gomoku
Version: 1.2.9
Release: alt4.1
Summary: Gomoku.app is an extended TicTacToe game for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.it/nicola/Applications/Gomoku/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
You win the game if you are able to put 5 of your pieces in a row,
column or diagonal. You loose if the computer does it before you. You
can play the game on boards of different size; the default size is 8 but
10 is also nice to play. The game has 6 different difficulty levels.

Features:

* Most of the development effort was concentrated on the artificial
  intelligence engine used by the computer while playing. Unlike most
  other engines, this engine is not designed to play very well, but
  rather to give you fun when you play against it.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.2.9-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt4
- Built with clang

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt1
- Initial build for Sisyphus

