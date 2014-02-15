%set_verify_elf_method unresolved=strict

Name: gnustep-timeui
Version: r715
Release: alt2.svn20090220
Summary: Make a bigger time and calendar ui framework
License: GPLv3+
Group: Graphical desktop/GNUstep
Url: https://savannah.nongnu.org/projects/gap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.savannah.nongnu.org/svn/gap/trunk/libs/timeui/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back
Requires: lib%name = %EVR

%description
TimeUI in the ss, a tiny framework which I've planned to make a bigger
time and calendar ui framework but it seems I don't have time to
finish until distantFuture. Now it's just a clock cell and control
that you can drag hands around.

%package -n lib%name
Summary: Shared libraries of TimeUI
Group: System/Libraries

%description -n lib%name
TimeUI in the ss, a tiny framework which I've planned to make a bigger
time and calendar ui framework but it seems I don't have time to
finish until distantFuture. Now it's just a clock cell and control
that you can drag hands around.

This package contains shared libraries of TimeUI.

%package -n lib%name-devel
Summary: Development files of TimeUI
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
TimeUI in the ss, a tiny framework which I've planned to make a bigger
time and calendar ui framework but it seems I don't have time to
finish until distantFuture. Now it's just a clock cell and control
that you can drag hands around.

This package contains development files of TimeUI.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2 -lm'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in TimeUI; do
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
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/TimeUI.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/TimeUI.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/TimeUI.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/TimeUI.framework/Headers

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r715-alt2.svn20090220
- Built with clang

* Thu Feb 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r715-alt1.svn20090220
- Initial build for Sisyphus

