%set_verify_elf_method unresolved=strict

Name: gnustep-Graphos
Version: 0.4
Release: alt1
Summary: Vector editor for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
Graphos is a vector drawing application centered around bezier paths.

Features:
* Bezier paths
* Boxes
* Circles
* V. 0.3 sports an improved, modeless, real-time inspector. New file
  format.
* V. 0.2 sports a new, modernized inspector.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

