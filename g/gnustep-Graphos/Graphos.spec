%set_verify_elf_method unresolved=strict

Name: gnustep-Graphos
Version: 0.3
Release: alt1
Summary: Vector editor for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

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

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

