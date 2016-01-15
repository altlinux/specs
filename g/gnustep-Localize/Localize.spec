%set_verify_elf_method unresolved=strict

Name: gnustep-Localize
Version: 20040424
Release: alt4.1
Summary: Application to aid in the translation of .strings files
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.eskimo.com/~pburns/Localize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Localize is an application to aid in the translation of .strings files.
.strings files must be distributed in ASCII encoding, which generally
isn't a convenient encoding to do translation in. As an example, its
rather difficult to enter Chinese characters into an ASCII encoded text
file. Localize will, with any luck, help out with this. Currently its
just a shell of an application, but sometime in the future I hope to
complete it.

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
%doc Documentation/*
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 20040424-alt4.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20040424-alt4
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20040424-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20040424-alt2
- Added Requires: gnustep-back

* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20040424-alt1
- Initial build for Sisyphus

