%set_verify_elf_method unresolved=strict

Name: gnustep-Cartotheque
Version: 0.1
Release: alt5.1
Summary: Managing notes on small cards
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Cartotheque.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.freebsd.org/pub/FreeBSD/ports/distfiles/Cartotheque-0.1.tar.gz
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
An application for managing notes on small cards (like punch cards :).
The application uses a directory based repository for cards with various
contents. Currently only one contents is supported, and that is RTF
contents (NSAttributedString) editable by a text view.

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
%doc *.txt
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt5.1
- NMU: Rebuild with libgnutls30.

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5
- Fixed menu file (by kostyalamer@)

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

