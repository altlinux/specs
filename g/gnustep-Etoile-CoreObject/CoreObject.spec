%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-CoreObject
Version: 0.5
Release: alt1.git20140306
Summary: Version-controlled object database
License: MIT
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/CoreObject.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator libdispatch-objc2-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel libsqlite3-devel
BuildPreReq: libssl-devel gcc-c++

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation

%description
CoreObject is a version-controlled object database, designed to be a
humane persistence layer for applications with a "never lose any work"
philosophy.

At the center is an ACID-compliant object store using SQLite, and built
on this are semantic merging, rich undo/redo support, collaborative
editing, and a transaction API for viewing database snapshots in memory
and batching changes for commit.

%package -n lib%name
Summary: Shared libraries of CoreObject
Group: System/Libraries

%description -n lib%name
CoreObject is a version-controlled object database, designed to be a
humane persistence layer for applications with a "never lose any work"
philosophy.

At the center is an ACID-compliant object store using SQLite, and built
on this are semantic merging, rich undo/redo support, collaborative
editing, and a transaction API for viewing database snapshots in memory
and batching changes for commit.

This package contains shared libraries of CoreObject.

%package -n lib%name-devel
Summary: Development files of CoreObject
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
CoreObject is a version-controlled object database, designed to be a
humane persistence layer for applications with a "never lose any work"
philosophy.

At the center is an ACID-compliant object store using SQLite, and built
on this are semantic merging, rich undo/redo support, collaborative
editing, and a transaction API for viewing database snapshots in memory
and batching changes for commit.

This package contains development files of CoreObject.

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
	documentation=no \
	AUXILIARY_CPPFLAGS="-I%_includedir/dispatch" \
	PROJECT_NAME=CoreObject

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=no \
	PROJECT_NAME=CoreObject

cp CoreObject/* \
	%buildroot%_libdir/GNUstep/Frameworks/CoreObject.framework/Headers/

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in CoreObject; do
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
%doc HACKING.md NEWS.md README.md TODO.md
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/CoreObject.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/CoreObject.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/CoreObject.framework/Headers
%_libdir/GNUstep/Frameworks/CoreObject.framework/Versions/0/Headers

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140306
- Initial build for Sisyphus

