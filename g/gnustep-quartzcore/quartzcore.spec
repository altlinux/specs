%set_verify_elf_method unresolved=strict

Name: gnustep-quartzcore
Version: 0.1
Release: alt2.svn20121018
Summary: Implementation of the Core Animation APIs
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-quartzcore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/quartzcore/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libGL-devel libcairo-devel gnustep-opal-devel
BuildPreReq: clang-devel libGLU-devel

Requires: lib%name = %EVR
Requires: gnustep-opal
Requires: gnustep-back

%description
This is GNUstep QuartzCore, an implementation of the Core Animation APIs
intended for use with GNUstep. It's implemented in Objective-C and C.

%package -n lib%name
Summary: Shared libraries of QuartzCore
Group: System/Libraries

%description -n lib%name
This is GNUstep QuartzCore, an implementation of the Core Animation APIs
intended for use with GNUstep. It's implemented in Objective-C and C.

This package contains shared libraries of QuartzCore.

%package -n lib%name-devel
Summary: Development files of QuartzCore
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This is GNUstep QuartzCore, an implementation of the Core Animation APIs
intended for use with GNUstep. It's implemented in Objective-C and C.

This package contains development files of QuartzCore.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lcairo -lGL -lopal -lgnustep-base -lobjc2 -lm'

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in QuartzCore; do
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
%doc ChangeLog README.markdown
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/QuartzCore.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/QuartzCore.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/QuartzCore.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/QuartzCore.framework/Headers

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.svn20121018
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20121018
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20121018
- Initial build for Sisyphus

