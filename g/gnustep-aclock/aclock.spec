%set_verify_elf_method unresolved=strict

Name: gnustep-aclock
Version: 0.3
Release: alt5
Summary: Analog Clock
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://gnu.ethz.ch/linuks.mine.nu/aclock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Analog Clock for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt5
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt4
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Applied patch from Debian

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Rebuilt with new gnustep-gui

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

