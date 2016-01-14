# spec by Konstantin Kogan (kostyalamer)

%set_verify_elf_method unresolved=strict

Name: gnustep-gmastermind
Version: 0.6
Release: alt4.1
Summary: GMastermind is a game for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
URL: http://www.nongnu.org/gap/gmastermind/

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
GMastermind is an implementation of the well-known Mastermind game.

Drag-and-drop colors from the palette or from the board itself. The
object is to determine the hidden combination of four colors. The game
may be played in two modes: with replacement, which means that colors
may repeat, and without replacement, which means that colors are unique.
The user selects a choice of four colors and "commits" them. The program
replies with an evaluation -- a black peg for a color that is placed
correctly, and a white peg for a color that is in the wrong position.
The user may make a total of eight queries.

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
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt4
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Rebuilt with new gnustep-gui

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

