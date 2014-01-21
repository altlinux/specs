%set_verify_elf_method unresolved=strict

Name: gnustep-IMImage
Version: 2004
Release: alt3
Summary: IMImage image Inspector for GWorkspace.app to preview many types of graphics formats
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GWorkspace.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel libImageMagick-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-gworkspace ghostscript

%description
IMImage image Inspector for GWorkspace.app to preview many types of
graphics formats not supported by NSImage utilizing Image Magick. The
following graphics formats are currently supported: art, bmp, cgm, eps,
fig, fpx, hpgl, ico, miff, mng, mvg, pbm, pcd, pcl, pcx, pgm, pict, pix,
pnm, ppm, psd, rla, rle, svg, tga, wmf, wpg, xbm, xcf, xpm, and xwd. It
can also be used to preview Type 1 and TrueType fonts.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/ImageMagick-6' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%buildroot

%files
%doc README
%_libdir/GNUstep

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt3
- Rebuilt with new gnustep-gui

* Sat Apr 20 2013 Anton Farygin <rider@altlinux.ru> 2004-alt2
- Rebuilt with new ImageMagick

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt1
- Initial build for Sisyphus

