%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-OgreKit
Version: 1.2.1
Release: alt1.svn20140213.1
Summary: Regular expression library written in Objective-C in Cocoa
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/OgreKit/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libOniGuruma-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
OgreKit is a regular expression library written in Objective-C in Cocoa.
It uses OniGuruma as regular expression engine.

%package -n lib%name
Summary: Shared libraries of OgreKit
Group: System/Libraries

%description -n lib%name
OgreKit is a regular expression library written in Objective-C in Cocoa.
It uses OniGuruma as regular expression engine.

This package contains shared libraries of OgreKit.

%package -n lib%name-devel
Summary: Development files of OgreKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
OgreKit is a regular expression library written in Objective-C in Cocoa.
It uses OniGuruma as regular expression engine.

This package contains development files of OgreKit.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=OgreKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=OgreKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in OgreKit; do
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

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc COPYING ChangeLog NEWS README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/OgreKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/OgreKit.framework/Versions/1/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/OgreKit.framework/Headers
%_libdir/GNUstep/Frameworks/OgreKit.framework/Versions/1/Headers

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.svn20140213.1
- NMU: Rebuild with libgnutls30.

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20140213
- Initial build for Sisyphus

