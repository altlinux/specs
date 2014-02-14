%set_verify_elf_method unresolved=strict

Name: gnustep-GSKrab
Version: 0.0.1
Release: alt4
Summary: GNUstep Keyboard Grabber
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GSKrab
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libX11-devel xorg-xproto-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
GS Krab is a framework and a daemon to enable GNUstep applications to
handle the special keys on multimedia keyboards. Since this would
require special hacks to work on different platform, and since those
differents platforms work differently, I thought putting those hacks
together in a centralized daemon would be the correct and clean way to
do things.

%package -n lib%name
Summary: Shared libraries of GS Krab
Group: System/Libraries

%description -n lib%name
GS Krab is a framework and a daemon to enable GNUstep applications to
handle the special keys on multimedia keyboards. Since this would
require special hacks to work on different platform, and since those
differents platforms work differently, I thought putting those hacks
together in a centralized daemon would be the correct and clean way to
do things.

This package contains shared libraries of GS Krab.

%package -n lib%name-devel
Summary: Development files of GS Krab
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
GS Krab is a framework and a daemon to enable GNUstep applications to
handle the special keys on multimedia keyboards. Since this would
require special hacks to work on different platform, and since those
differents platforms work differently, I thought putting those hacks
together in a centralized daemon would be the correct and clean way to
do things.

This package contains development files of GS Krab.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

pushd %buildroot%_libdir
for j in GSKrab; do
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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/GSKrab.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/GSKrab.framework/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/GSKrab.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/GSKrab.framework/Headers

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt4
- Built with clang

* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus

