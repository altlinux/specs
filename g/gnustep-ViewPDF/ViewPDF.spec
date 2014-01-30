%set_verify_elf_method unresolved=strict

Name: gnustep-ViewPDF
Version: 0.2
Release: alt2
Summary: Portable Document Format (PDF) viewer for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/jessie/viewpdf.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-PopplerKit-devel

Requires: gnustep-PopplerKit
Requires: gnustep-back

%description
ViewPDF is an application to view and navigate in PDF documents.

Key Features:
* Zoom
* Keyboard shortcuts for fast navigation

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

%files
%doc docs/*
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

