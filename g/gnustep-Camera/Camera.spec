%set_verify_elf_method unresolved=strict

Name: gnustep-Camera
Version: 0.8
Release: alt7
Summary: Camera downloads files from your digital camera
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Camera.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libgphoto2-devel

Requires: gnustep-back

%description
A simple tool to download photos from a digital camera.

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
%doc Documentation/README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.8-alt7
- Rebuild with new icu

* Fri Jan 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt6
- Rebuilt with new libgphoto2

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt5
- Fixed menu file (by kostyalamer@)

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt4
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

