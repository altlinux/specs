%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-PaneKit
Version: 1.0
Release: alt1.svn20140217.1
Summary: Provides various features to build flexible pane window
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/PaneKit/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-UnitKit-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-UnitKit

%description
PaneKit is a framework which provides various features to build
flexible pane window in any GNUstep or Cocoa applications.
PKPanesController controls the main user interface
and several presentations are available.
Panes can be build in bundle of Nib or programmingly.
They are registered in PKPaneRegistry and displayed by
PKPanesController.

PKPreferencesController and PKPreferencesPaneRegistry
are designed to handle preferences.
It includes an NSPreferencePane implementation (following Cocoa API).

%package -n lib%name
Summary: Shared libraries of PaneKit
Group: System/Libraries

%description -n lib%name
PaneKit is a framework which provides various features to build
flexible pane window in any GNUstep or Cocoa applications.
PKPanesController controls the main user interface
and several presentations are available.
Panes can be build in bundle of Nib or programmingly.
They are registered in PKPaneRegistry and displayed by
PKPanesController.

PKPreferencesController and PKPreferencesPaneRegistry
are designed to handle preferences.
It includes an NSPreferencePane implementation (following Cocoa API).

This package contains shared libraries of PaneKit.

%package -n lib%name-devel
Summary: Development files of PaneKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
PaneKit is a framework which provides various features to build
flexible pane window in any GNUstep or Cocoa applications.
PKPanesController controls the main user interface
and several presentations are available.
Panes can be build in bundle of Nib or programmingly.
They are registered in PKPaneRegistry and displayed by
PKPanesController.

PKPreferencesController and PKPreferencesPaneRegistry
are designed to handle preferences.
It includes an NSPreferencePane implementation (following Cocoa API).

This package contains development files of PaneKit.

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
	PROJECT_NAME=PaneKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=PaneKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in PaneKit; do
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
%doc ChangeLog README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/PaneKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/PaneKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/PaneKit.framework/Headers
%_libdir/GNUstep/Frameworks/PaneKit.framework/Versions/0/Headers

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt1.svn20140217.1
- NMU: Rebuild with libgnutls30.

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20140217
- Initial build for Sisyphus

