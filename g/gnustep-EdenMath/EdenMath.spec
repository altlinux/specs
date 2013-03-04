%set_verify_elf_method unresolved=strict

Name: gnustep-EdenMath
Version: 1.1.1
Release: alt1.a
Summary: Scientific calculator for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

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
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_LOCAL_ROOT=%buildroot

%files
%doc *.rtf
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.a
- Initial build for Sisyphus

