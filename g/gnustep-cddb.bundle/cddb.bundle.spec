%set_verify_elf_method unresolved=strict

Name: gnustep-cddb.bundle
Version: 0.2
Release: alt1
Summary: GNUstep bundle for cddb access
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel

%description
cddb.bundle is a GNUstep bundle for cddb access.

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
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

%files
%doc README TUTORIAL
%_libdir/GNUstep

%changelog
* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

