%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ProjectManager
Version: 0.1
Release: alt1.git20120112
Summary: Work-in-progress compositing window manager for the Etoile environment
License: MIT
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/ProjectManager.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-EtoileUI-devel
BuildPreReq: gnustep-Etoile-XWindowServerKit-devel
BuildPreReq: libxcb-devel libxcbutil-devel libxcb-render-util-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileUI
Requires: gnustep-Etoile-XWindowServerKit

%description
This is a (work-in-progress) compositing window manager for the Etoile
environment.

%package -n lib%name
Summary: Shared libraries of Etoile's ProjectManager
Group: System/Libraries

%description -n lib%name
This is a (work-in-progress) compositing window manager for the Etoile
environment.

This package contains shared libraries of Etoile's ProjectManager.

%package -n lib%name-devel
Summary: Development files of Etoile's ProjectManager
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This is a (work-in-progress) compositing window manager for the Etoile
environment.

This package contains development files of Etoile's ProjectManager.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=ProjectManager

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ProjectManager

pushd %buildroot%_libdir
for j in XCBKit; do
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
%doc README
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/XCBKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/XCBKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/XCBKit.framework/Headers
%_libdir/GNUstep/Frameworks/XCBKit.framework/Versions/0/Headers

%changelog
* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120112
- Initial build for Sisyphus

