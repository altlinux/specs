%set_verify_elf_method unresolved=strict

Name: gnustep-HighlighterKit
Version: 0.1.3
Release: alt2
Summary: Framework needed by Gemas and Project Manager
License: LGPL-2.1 and GFDL-1.2+
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/HighlighterKit
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
HighlighterKit provides a framework for highlighting and coloring syntax
in code editors. The Project Manager IDE and code editor Gemas.app makes
use of it, yet it can be included in other applications.

%package -n lib%name
Summary: Shared libraries of GNUstep HighlighterKit
Group: System/Libraries

%description -n lib%name
HighlighterKit provides a framework for highlighting and coloring syntax
in code editors. The Project Manager IDE and code editor Gemas.app makes
use of it, yet it can be included in other applications.

This package contains shared libraries of GNUstep HighlighterKit.

%package -n lib%name-devel
Summary: Development files of GNUstep HighlighterKit
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
HighlighterKit provides a framework for highlighting and coloring syntax
in code editors. The Project Manager IDE and code editor Gemas.app makes
use of it, yet it can be included in other applications.

This package contains development files of GNUstep HighlighterKit.

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
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in HighlighterKit; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

%files
%doc ChangeLog README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt2
- Build without libgnustep-objc2-devel.
- Fix License tag.

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Version 0.1.3

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt4
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Rebuilt with new gnustep-gui

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

