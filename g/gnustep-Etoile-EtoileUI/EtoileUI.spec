%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-EtoileUI
Version: 0.4.1
Release: alt1.git20140227
Summary: Provides a uniform tree representation for graphical objects
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/EtoileUI.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-CoreObject-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-IconKit-devel libdispatch-objc2-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-CoreObject gnustep-Etoile-IconKit

%description
EtoileUI is a high-level OOUI toolkit that provides a uniform tree
representation for graphical objects on top of the AppKit. All User
Interface concerns such as layouts, event handlers, styles, model
objects etc. intends to be implemented as pluggable aspects. It also
shares the same interfaces as other CoreObject systems. The combination
of these three key features makes possible to inspect and reshape both
User Interface and model objects at runtime through direct manipulation.
It comes with a library of layouts where each one encapsulate a custom
and pluggable UI presentation.

%package -n lib%name
Summary: Shared libraries of EtoileUI
Group: System/Libraries

%description -n lib%name
EtoileUI is a high-level OOUI toolkit that provides a uniform tree
representation for graphical objects on top of the AppKit. All User
Interface concerns such as layouts, event handlers, styles, model
objects etc. intends to be implemented as pluggable aspects. It also
shares the same interfaces as other CoreObject systems. The combination
of these three key features makes possible to inspect and reshape both
User Interface and model objects at runtime through direct manipulation.
It comes with a library of layouts where each one encapsulate a custom
and pluggable UI presentation.

This package contains shared libraries of EtoileUI.

%package -n lib%name-devel
Summary: Development files of EtoileUI
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
EtoileUI is a high-level OOUI toolkit that provides a uniform tree
representation for graphical objects on top of the AppKit. All User
Interface concerns such as layouts, event handlers, styles, model
objects etc. intends to be implemented as pluggable aspects. It also
shares the same interfaces as other CoreObject systems. The combination
of these three key features makes possible to inspect and reshape both
User Interface and model objects at runtime through direct manipulation.
It comes with a library of layouts where each one encapsulate a custom
and pluggable UI presentation.

This package contains development files of EtoileUI.

%package docs
Summary: Documentation for EtoileUI
Group: Development/Documentation
BuildArch: noarch

%description docs
EtoileUI is a high-level OOUI toolkit that provides a uniform tree
representation for graphical objects on top of the AppKit. All User
Interface concerns such as layouts, event handlers, styles, model
objects etc. intends to be implemented as pluggable aspects. It also
shares the same interfaces as other CoreObject systems. The combination
of these three key features makes possible to inspect and reshape both
User Interface and model objects at runtime through direct manipulation.
It comes with a library of layouts where each one encapsulate a custom
and pluggable UI presentation.

This package contains documentation for EtoileUI.

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
	AUXILIARY_CPPFLAGS="-I%_includedir/dispatch"

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in EtoileUI; do
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

install -d %buildroot%_docdir/GNUstep/EtoileUI
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/EtoileUI/

%files
%doc ChangeLog NEWS README SCRATCHPAD TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/EtoileUI.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/EtoileUI.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/EtoileUI.framework/Headers
%_libdir/GNUstep/Frameworks/EtoileUI.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140227
- Initial build for Sisyphus

