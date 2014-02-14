Name: gnustep-cenon
Version: 4.0.2
Release: alt2
Summary: Vector graphics tool for GNUstep
License: vhfPL
Group: Graphical desktop/GNUstep
Url: http://www.cenon.info/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-CenonLibrary

%description
Cenon is a vector graphics tool for GNUstep. It is built upon a modular
graphical core, and offers a variety of applications beyond desktop
publishing.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

TOPDIR=$PWD
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-DMAXFLOAT=3.40282347e+38F -I$TOPDIR -I$TOPDIR/GraphicObjects.subproj"
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

install -d %buildroot%_libdir/GNUstep
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc NEWS README COPYRIGHT LICENSE ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Built with clang

* Mon Mar 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

