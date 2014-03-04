%set_verify_elf_method unresolved=strict

Name: gnustep-netclasses
Version: 1.06
Release: alt3.svn20131019
Summary: Asynchronous networking framework for GNUstep and Mac OS X
License: LGPLv2
Group: Graphical desktop/GNUstep
Url: http://netclasses.aeruder.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.savannah.nongnu.org/svn/gap/trunk/libs/netclasses/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Asynchronous networking framework for GNUstep and Mac OS X. Has built-in
support for line-based protocols, IRC, and raw TCP/IP streams.

%package -n lib%name
Summary: Shared libraries of netclasses
Group: System/Libraries

%description -n lib%name
Asynchronous networking framework for GNUstep and Mac OS X. Has built-in
support for line-based protocols, IRC, and raw TCP/IP streams.

This package contains shared libraries of netclasses.

%package -n lib%name-devel
Summary: Development files of netclasses
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Asynchronous networking framework for GNUstep and Mac OS X. Has built-in
support for line-based protocols, IRC, and raw TCP/IP streams.

This package contains development files of netclasses.

%package docs
Summary: Documentation for netclasses
Group: Documentation
BuildArch: noarch

%description docs
Asynchronous networking framework for GNUstep and Mac OS X. Has built-in
support for line-based protocols, IRC, and raw TCP/IP streams.

This package contains documentation for netclasses.

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
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in netclasses; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/1.06/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/1.06/$i ||:
			rm GNUstep/Frameworks/$j.framework/Versions/1.06/$j ||:
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/1.06/$j ||:
		done
	done
done
popd

%files
%doc README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/1.06/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/1.06/Headers

%files docs
%_docdir/GNUstep

%changelog
* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.06-alt3.svn20131019
- Snapshot from svn

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.06-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.06-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.06-alt1
- Initial build for Sisyphus

