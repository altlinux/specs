%set_verify_elf_method unresolved=strict

Name: gnustep-quartzcore
Version: 0.1
Release: alt1.git20121018
Summary: Implementation of the Core Animation APIs
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: https://github.com/gnustep/gnustep-quartzcore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-quartzcore.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libGL-devel libcairo-devel gnustep-opal-devel
BuildPreReq: clang-devel libGLU-devel

Requires: lib%name = %EVR
Requires: gnustep-opal

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

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lcairo -lGL -lopal -lgnustep-base -lobjc2 -lm' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

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
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20121018
- Initial build for Sisyphus

