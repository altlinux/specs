%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-AZSwitch
Version: r7983
Release: alt2.svn20130128.1
Summary: Experimental application for window switching
License: MIT
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Services/Private/AZSwitch/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-XWindowServerKit-devel
BuildPreReq: gnustep-Etoile-EtoileUI-devel

Requires: gnustep-back gnustep-Etoile-XWindowServerKit
Requires: gnustep-Etoile-EtoileUI

%description
AZSwitch is an experimental application for window switching.
The main challenge is how to track key and mouse input
and show minimature window.
Unlike AZDock, which is application-based, AZSwitch is window-based.
Therefore, they are not compatible to each other in implementation.

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
	PROJECT_NAME=AZSwitch

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=AZSwitch

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> r7983-alt2.svn20130128.1
- NMU: Rebuild with libgnutls30.

* Mon Mar 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7983-alt2.svn20130128
- Added menu file (thnx kostyalamer@)

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7983-alt1.svn20130128
- Initial build for Sisyphus

