%set_verify_elf_method unresolved=strict

Name: gnustep-CameraKit
Version: 20041011
Release: alt4
Summary: A simple wrapper to libgphoto
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://home.gna.org/gsimageapps/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libgphoto2-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
A simple wrapper to libgphoto.

%package -n lib%name
Summary: Shared libraries of CameraKit
Group: System/Libraries

%description -n lib%name
A simple wrapper to libgphoto.

This package contains shared libraries of CameraKit.

%package -n lib%name-devel
Summary: Development files of CameraKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
A simple wrapper to libgphoto.

This package contains development files of CameraKit.

%prep
%setup
%patch1 -p2

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in CameraKit; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

%files
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/CameraKit.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/CameraKit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/CameraKit.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/CameraKit.framework/Headers

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 20041011-alt4
- Build without libgnustep-objc2-devel.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041011-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041011-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041011-alt1
- Initial build for Sisyphus

