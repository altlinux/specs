%set_verify_elf_method unresolved=strict

Name: gnustep-Ghack
Version: 0.2
Release: alt4.git20130613
Summary: Graphical nethack
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/v-zor/ninjacode.git
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Minimal tile engine graphics support.

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
%doc ChangeLog HACKING README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt4.git20130613
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3.git20130613
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2.git20130613
- Rebuilt with new gnustep-gui

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130613
- Version 0.2

* Sat Mar 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt2
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

