# spec by Konstantin Kogan (kostyalamer)

%set_verify_elf_method unresolved=strict

Name: gnustep-gmastermind
Version: 0.6
Release: alt1
Summary: GMastermind is a game for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
URL: http://www.nongnu.org/gap/gmastermind/

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

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
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

