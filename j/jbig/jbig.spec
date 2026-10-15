Name: jbig
Version: 2.2
Release: alt1

Summary: JBIG-KIT lossless image compression library

License: GPLv2+
Group: Graphics
Url: http://www.cl.cam.ac.uk/~mgk25/jbigkit/

# Source-url: http://www.cl.cam.ac.uk/~mgk25/download/jbigkit-%version.tar.gz
Source: %name-%version.tar

Patch: jbigkit-2.2-shlib.patch

# soname = library version (as in Fedora): 2.2 changed struct jbg_dec_state
%define sover 2.2

%package -n libjbig%sover
Summary: JBIG-KIT lossless image compression library (shared library)
Group: System/Libraries

%package -n libjbig-devel
Summary: JBIG-KIT lossless image compression library (header files)
Group: Development/C
Requires: libjbig%sover = %EVR

%package -n libjbig-devel-static
Summary: JBIG-KIT lossless image compression library (static library)
Group: Development/C
Requires: libjbig-devel = %EVR

%package utils
Summary: JBIG-KIT lossless image compression utilities
Group: Graphics
Requires: libjbig%sover = %EVR
Provides: jbigkit = %version
Obsoletes: jbigkit <= %version

%description
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface (similar to the converters found in netpbm).

JBIG-KIT implements the specification:
    ISO/IEC 11544:1993 and ITU-T Recommendation T.82(1993):
     Information technology - Coded representation of picture and audio
     information - Progressive bi-level image compression.

which is commonly referred to as the "JBIG1 standard"

%description -n libjbig%sover
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface (similar to the converters found in netpbm).

JBIG-KIT implements the specification:
    ISO/IEC 11544:1993 and ITU-T Recommendation T.82(1993):
     Information technology - Coded representation of picture and audio
     information - Progressive bi-level image compression.

which is commonly referred to as the "JBIG1 standard"

%description -n libjbig-devel
JBIG is a highly effective lossless compression algorithm for bi-level
images (one bit per pixel), which is particularly suitable for scanned
document pages.

This package is only needed if you plan to develop or compile
applications which requires the libjbig library.

%description -n libjbig-devel-static
JBIG is a highly effective lossless compression algorithm for bi-level
images (one bit per pixel), which is particularly suitable for scanned
document pages.

This package contains static JBIG library.

%description utils
JBIG is a highly effective lossless compression algorithm for bi-level
images (one bit per pixel), which is particularly suitable for scanned
document pages.

%prep
%setup
%patch -p1

%build
%make_build RPM_OPT_FLAGS='%optflags' SOVER=%sover

LD_LIBRARY_PATH=$PWD/libjbig make test

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_man1dir}
install -p -m755 pbmtools/{jbgtopbm,pbmtojbg} %buildroot%_bindir/
install -p -m644 pbmtools/*.1 %buildroot%_man1dir/
install -p -m0644 libjbig/jbig.h %buildroot%_includedir
install -p -m0644 libjbig/jbig85.h %buildroot%_includedir
install -p -m0644 libjbig/jbig_ar.h %buildroot%_includedir

install -p -m0755 libjbig/libjbig.so.%sover %buildroot%_libdir
install -p -m0755 libjbig/libjbig85.so.%sover %buildroot%_libdir
ln -sf libjbig.so.%sover %buildroot%_libdir/libjbig.so
ln -sf libjbig85.so.%sover %buildroot%_libdir/libjbig85.so

%if_enabled static
cp -a libjbig/libjbig.a %buildroot%_libdir/
%endif

%define pkgdocdir %_docdir/jbig-%version
mkdir -p %buildroot%pkgdocdir
cp -a ANNOUNCE CHANGES %buildroot%pkgdocdir/
cp -a INSTALL %buildroot%pkgdocdir/README
#cp -a libjbig/jbig.doc %buildroot%pkgdocdir/jbig.txt

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make -k test

%files -n libjbig%sover
%_libdir/libjbig.so.%sover
%_libdir/libjbig85.so.%sover
%dir %pkgdocdir
%pkgdocdir/ANNOUNCE
%pkgdocdir/CHANGES
%pkgdocdir/README

%files -n libjbig-devel
%_libdir/libjbig.so
%_libdir/libjbig85.so
%_includedir/jbig*.h
%dir %pkgdocdir
#pkgdocdir/jbig.txt

%if_enabled static
%files -n libjbig-devel-static
%_libdir/libjbig.a
%endif

%files utils
%_bindir/jbgtopbm
%_bindir/pbmtojbg
%_man1dir/jbgtopbm.*
%_man1dir/pbmtojbg.*

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2
- rebase shared library patch, drop patches merged upstream
- change soname to libjbig.so.2.2, libjbig85.so.2.2 (libjbig2.2): 2.2 adds
  maxmem field to public struct jbg_dec_state (ABI break)

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- cleanup spec, applied patches from Fedora
- use real soname libjbig.so.2.1
- add soname libjbig85.so.2.1
- build lib package as libjbig2.1

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1
- Version 2.1

* Fri Jul 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt2
- %name-devel: packaged /usr/include/jbig_ar.h (closes: #25869).
- Enabled test suite.

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt3
- Rebuilt for soname set-versions

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.6-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libjbig
  * postun_ldconfig for libjbig
  * postclean-05-filetriggers for spec file

* Sun Aug 19 2007 Alexey Tourbin <at@altlinux.ru> 1.6-alt2
- rebuild

* Wed Aug 25 2004 Alexey Tourbin <at@altlinux.ru> 1.6-alt1
- 1.2 -> 1.6, changed soname
- use strict dependencies between subpackages
- moved libjbig.a to libjbig-devel-static (not packaged by default)

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.2-ipl3mdk
- rebuild

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.2-ipl2mdk
- rebuild

* Mon Feb 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.2-ipl1mdk
- Libification.
- RE adaptions.

* Tue Dec 26 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.2-1mdk
- initial release for OpenDX.
