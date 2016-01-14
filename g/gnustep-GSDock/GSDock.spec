%set_verify_elf_method unresolved=strict

Name: gnustep-GSDock
Version: 0.0.1
Release: alt3.1
Summary: GSDock is a dock written using the GNUstep API
License: GPL
Group: Graphical desktop/GNUstep
Url: http://gsdock.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
GSDock is a dock written using the GNUstep (OpenStep) API. It is a
hybrid of the traditional NeXTstep Dock and the newer OS X Dock.

* Accepts dragged executables.
* Animates launching application icons.
* OpenStep/NeXTStep look with a twist of OS X functionality.
* Application tiles shrink so the dock is able to "swallow" as many
  applications as you want.
* Accepts dragged documents onto the tiles of applications which can
  open the dragged document.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt3.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3
- Built with clang

* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2
- Added menu file (thnx kostyalamer@)

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus

