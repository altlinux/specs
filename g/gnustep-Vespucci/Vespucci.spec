%set_verify_elf_method unresolved=strict

Name: gnustep-Vespucci
Version: 0.1
Release: alt4.cvs20140125.1
Summary: Vespucci is a navigator for the World Wide Web
License: Free
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/vespucci/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/user-apps/Vespucci
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-simplewebkit-devel

Requires: gnustep-simplewebkit
Requires: gnustep-back

%description
Vespucci is a web browser which uses a WebKit-compatible rendering
engine, thus it can either use Apple's WebKit or GNUstep's SimpleWebKit.

Features:

* multiple-document support, with recent document list
* standard back/forward buttons
* bookmarks, in Safari-compatible format (it can read safari bookmarks
  directly)
* Workspace integration
* webloc link file support (just copy over the file from Mac)
* Open URL service
* Cookie management

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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.cvs20140125.1
- NMU: Rebuild with libgnutls30.

* Mon Feb 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.cvs20140125
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.cvs20140125
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.cvs20140125
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140125
- Initial build for Sisyphus

