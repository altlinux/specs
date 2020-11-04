%set_verify_elf_method unresolved=strict

Name: gnustep-GRubik
Version: 0.1
Release: alt6
Summary: GRubik is a virtual 3D Rubik's cube for you to solve
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GRubik.app
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
GRubik is a virtual 3D Rubik's cube for you to solve.

Features:

* simple but functional and fast 3D
* a smart scramble that ensures you get a solvable cube
* interesting code that you might enjoy reading and which uses a variety
  of programming techniques.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKE_STRICT_V2_MODE=no \
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/GRubik.app/GRubik \
	%buildroot%_bindir/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Built with clang

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

