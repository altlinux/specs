%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ObjectManager
Version: r9902
Release: alt2.git20131217
Summary: Etoile's ObjectManager
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/ObjectManager.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-pbxbuild
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-CoreObject-devel libdispatch-objc2-devel
BuildPreReq: gnustep-Etoile-EtoileUI-devel gnustep-Etoile-IconKit-devel

Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-CoreObject gnustep-Etoile-EtoileUI
Requires: gnustep-Etoile-IconKit

%description
Etoile's ObjectManager.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

pbxbuild -p ObjectManager.xcodeproj -g

LIBS="-lCoreObject -lEtoileUI -lIconKit -lEtoileFoundation"
%make -C pbxbuild \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	AUXILIARY_CPPFLAGS="-I%_includedir/dispatch" \
	CONFIG_SYSTEM_LIBS="$LIBS" \
	PROJECT_NAME=ObjectManager

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std -C pbxbuild GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ObjectManager

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Mar 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9902-alt2.git20131217
- Added menu file (thnx kostyalamer@)

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r9902-alt1.git20131217
- Initial build for Sisyphus

