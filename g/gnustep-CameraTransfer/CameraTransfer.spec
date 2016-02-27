%set_verify_elf_method unresolved=strict

Name: gnustep-CameraTransfer
Version: 0.3
Release: alt8
Summary: Get pictures from a digital camera
License: GPL
Group: Graphical desktop/GNUstep
Url: http://sourceforge.net/projects/cameratransfer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: BCell.m
Source2: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libgphoto2-devel

Requires: gnustep-back

%description
CameraTransfer is a GNUstep front-end to the gphoto2 library.
It is able to transfer files from the camera to the computer, delete
files from the camera etc.

%prep
%setup
install -m644 %SOURCE1 .

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

install -p -D -m644 %SOURCE2 %buildroot%_menudir/%name

%files
%doc README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.3-alt8
- Rebuilt with new icu

* Fri Jan 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt7
- Rebuilt with new libgphoto2

* Thu Mar 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt6
- Fixed segfault

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt5
- Fixed menu file (by kostyalamer@)

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

