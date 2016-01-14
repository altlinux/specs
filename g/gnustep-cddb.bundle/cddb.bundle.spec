%set_verify_elf_method unresolved=strict

Name: gnustep-cddb.bundle
Version: 0.2
Release: alt6.1
Summary: GNUstep bundle for cddb access
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNUstep
Url: http://gsburn.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
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
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt6.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt6
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt5
- Added Requires: gnustep-back

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt4
- Fixed build

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Rebuilt with new gnustep-gui

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Moved header into %_includedir
- Added devel subpackage

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

