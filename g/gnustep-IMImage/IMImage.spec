%set_verify_elf_method unresolved=strict

Name: gnustep-IMImage
Version: 2004
Release: alt6.1
Summary: IMImage image Inspector for GWorkspace.app to preview many types of graphics formats
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/GWorkspace.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel libImageMagick-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-gworkspace ghostscript
Requires: gnustep-back

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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%_includedir/ImageMagick-6'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_SYSTEM_ROOT=%buildroot

%files
%doc README
%_libdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 2004-alt6.1
- NMU: Rebuild with libgnutls30.

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 2004-alt6
- Rebuild with new ImageMagick

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt5
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt4
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt3
- Rebuilt with new gnustep-gui

* Sat Apr 20 2013 Anton Farygin <rider@altlinux.ru> 2004-alt2
- Rebuilt with new ImageMagick

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2004-alt1
- Initial build for Sisyphus

