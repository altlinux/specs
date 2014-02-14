%set_verify_elf_method unresolved=strict

Name: gnustep-Gridlock
Version: 1.10
Release: alt4
Summary: A collection of grid-based board games for GNUstep
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/jessie/gridlock.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Gridlock is a collection of grid-based board games for GNUstep,
including Ataxx, Reversi, Gomoku, Connect Four, Breakthrough, Glass
Bead, Hexapawn, Quad Wrangle, Cats and Dogs and Moray Eels. You can play
against another person or computer opponents of varying difficulty, even
over the network.

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

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README.GNUstep readme.html
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt4
- Built with clang

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Initial build for Sisyphus

