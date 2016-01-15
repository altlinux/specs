%set_verify_elf_method unresolved=strict

Name: gnustep-EdenMath
Version: 1.1.1
Release: alt5.a.1
Summary: Scientific calculator for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/EdenMath.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
EdenMath is a scientific calculator which does standard arithmetic,
probability, and trigonometric functions.

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

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc *.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt5.a.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt5.a
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt4.a
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3.a
- Rebuilt with new gnustep-gui

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.a
- Added menu file (thnx kostyalamer@)

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.a
- Initial build for Sisyphus

