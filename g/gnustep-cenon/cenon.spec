Name: gnustep-cenon
Version: 4.0.2
Release: alt1
Summary: Vector graphics tool for GNUstep
License: vhfPL
Group: Graphical desktop/GNUstep
Url: http://www.cenon.info/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

Requires: gnustep-CenonLibrary

%description
Cenon is a vector graphics tool for GNUstep. It is built upon a modular
graphical core, and offers a variety of applications beyond desktop
publishing.

%prep
%setup

%build
TOPDIR=$PWD
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-O2 -DMAXFLOAT=3.40282347e+38F -I$TOPDIR -I$TOPDIR/GraphicObjects.subproj" \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
install -d %buildroot%_libdir/GNUstep
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc NEWS README COPYRIGHT LICENSE ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Mar 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus

