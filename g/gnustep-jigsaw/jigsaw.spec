# spec by Konstantin Kogan (kostyalamer)

%set_verify_elf_method unresolved=strict

Name: gnustep-jigsaw
Version: 0.8
Release: alt1
Summary: Jigsaw is a game for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
URL: http://gap.nongnu.org/jigsaw/

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
Jigsaw - GNUstep game!

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
* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

