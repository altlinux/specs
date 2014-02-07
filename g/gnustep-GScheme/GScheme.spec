%set_verify_elf_method unresolved=strict

Name: gnustep-GScheme
Version: 0.6.1
Release: alt3
Summary: GNUstep-aware scheme interpreter
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.freshports.org/lang/gscheme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel flex
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
A GNUstep-aware scheme interpreter. Includes many examples, e.g. the
sieve of Erathostenes to compute primes, a Koch curve plotter,
mandelbrot set, graphs of various functions etc. GScheme is fully tail
recursive. The garbage collector bypasses GNUstep's retain/release
mechanism in order to deal with circular data structures. GScheme is
document-based and you can edit more than one file at the same time.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc NOTES USAGE
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

