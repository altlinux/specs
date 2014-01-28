%set_verify_elf_method unresolved=strict

Name: gnustep-cddb.bundle
Version: 0.2
Release: alt4
Summary: GNUstep bundle for cddb access
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
cddb.bundle is a GNUstep bundle for cddb access.

%package devel
Summary: Development files of cddb.bundle
Group: Development/Objective-C
Requires: %name = %EVR

%description devel
cddb.bundle is a GNUstep bundle for cddb access.

This package contains development files of cddb.bundle.

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
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

install -d %buildroot%_includedir
ln -s %_libdir/GNUstep/Headers/Cddb \
	%buildroot%_includedir/

%files
%doc README TUTORIAL
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Headers

%files devel
%_includedir/*
%_libdir/GNUstep/Headers

%changelog
* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt4
- Fixed build

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Rebuilt with new gnustep-gui

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Moved header into %_includedir
- Added devel subpackage

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

