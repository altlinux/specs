%set_verify_elf_method unresolved=strict

Name: gnustep-EdenMath
Version: 1.1.1
Release: alt3.a
Summary: Scientific calculator for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
EdenMath is a scientific calculator which does standard arithmetic,
probability, and trigonometric functions.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_LOCAL_ROOT=%buildroot

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc *.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3.a
- Rebuilt with new gnustep-gui

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.a
- Added menu file (thnx kostyalamer@)

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.a
- Initial build for Sisyphus

