%set_verify_elf_method unresolved=strict

Name: gnustep-GSPdf
Version: 0.5
Release: alt1
Summary: Postscript and Pdf Viewer for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: libgs-devel gnustep-base-devel gnustep-gui-devel

%description
GSPdf is a Pdf and PostScript file viewer. It is based on GhostScript
which it calls at runtime to rasterize the pages.

GSPdf works perfectly as a native application for Print Preview. Once
installed, GNUstep will recognize it and use it without further setup.

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
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

