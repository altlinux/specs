%set_verify_elf_method unresolved=strict

Name: gnustep-LapisPuzzle
Version: 1.2
Release: alt2
Summary: Tetris-like game where each player is effected by the others game play
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
LapisPuzzle is a Tetris-like game where each player is effected by the
others game play. When one player clears blocks, the other gets more put
on! Attractive graphics as well.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ANNOUNCE ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Mar 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

