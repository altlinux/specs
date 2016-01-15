%set_verify_elf_method unresolved=strict

Name: gnustep-Affiche
Version: 0.6.0
Release: alt5.1
Summary: An application to "stick" little notes on the desktop
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/jessie/affiche.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Affiche is a little application that allows people to "stick" little
notes on their computer desktop. It was made for the GNUstep
environment.

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
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt5.1
- NMU: Rebuild with libgnutls30.

* Tue Mar 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt5
- Fixed menu file (by kostyalamer@)

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt4
- Built with clang

* Sun Feb 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

