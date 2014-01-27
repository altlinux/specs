%set_verify_elf_method unresolved=strict

Name: gnustep-OresmeKit
Version: 0.1
Release: alt1.cvs20140127
Summary: Oresme is a plotting framework for GNUstep
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/oresmekit/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR

%description
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

The kit offers custom Views that can be embedded in the application and
display data at need.

Why OresmeKit? In honour of Nicolas Oresme the antique philosopher who
thought about coordinates long before Cartesius. Because Cartesius was
too predictable as a name and too tied to X-Y plotting, while OresmeKit
shall support more chart types in the future.

%package -n lib%name
Summary: Shared libraries of OresmeKit
Group: System/Libraries

%description -n lib%name
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

This package contains shared libraries of OresmeKit.

%package -n lib%name-devel
Summary: Development files of OresmeKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

This package contains development files of OresmeKit.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2 -lm' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for j in OresmeKit; do
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
%exclude %_libdir/GNUstep/Frameworks/OresmeKit.framework/Versions/0.1/Headers
%exclude %_libdir/GNUstep/Frameworks/OresmeKit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/OresmeKit.framework/Versions/0.1/Headers
%_libdir/GNUstep/Frameworks/OresmeKit.framework/Headers

%changelog
* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140127
- Initial build for Sisyphus

