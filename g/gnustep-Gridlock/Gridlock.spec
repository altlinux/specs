%set_verify_elf_method unresolved=strict

Name: gnustep-Gridlock
Version: 1.10
Release: alt1
Summary: A collection of grid-based board games for GNUstep
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/jessie/gridlock.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
Gridlock is a collection of grid-based board games for GNUstep,
including Ataxx, Reversi, Gomoku, Connect Four, Breakthrough, Glass
Bead, Hexapawn, Quad Wrangle, Cats and Dogs and Moray Eels. You can play
against another person or computer opponents of varying difficulty, even
over the network.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -DGNU_RUNTIME' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

%files
%doc README.GNUstep readme.html
%_bindir/*
%_libdir/GNUstep

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Initial build for Sisyphus

