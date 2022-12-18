Name: libtiff
Version: 4.4.0
Release: alt2

Summary: Library of functions for manipulating TIFF format image files
License: BSD-style
Group: System/Libraries
Url: http://www.remotesensing.org/libtiff/

# git://git.altlinux.org/gears/l/%name
Source: %name-%version-%release.tar

%def_disable static
%def_enable cxx

BuildRequires: gcc-c++ libSM-devel libXi-devel libXmu-devel libfreeglut-devel libjbig-devel libjpeg-devel liblzma-devel libwebp-devel libzstd-devel zlib-devel
BuildRequires: libdeflate-devel
%description
This package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

%package -n libtiff5
Summary: Library of functions for manipulating TIFF format image files
Group: System/Libraries

%package utils
Summary: Programs for manipulating TIFF format image files
Group: Graphics
Requires: libtiff5 = %version-%release

%package -n tiffgt
Summary: Program for viewing TIFF format image files
Group: Graphics
Requires: libtiff5 = %version-%release

%package devel
Summary: Development files for programs which will use the tiff library
Group: Development/C
Requires: libtiff5 = %version-%release
Provides: libtiff5-devel
Obsoletes: libtiff5-devel

%package devel-static
Summary: Static tiff library
Group: Development/C
Requires: %name-devel = %version-%release

%package -n libtiffxx5
Summary: TIFF I/O C++ shared library
Group: System/Libraries
Requires: libtiff5 = %version-%release

%package -n libtiffxx-devel
Summary: TIFF I/O C++ development library and header files
Group: Development/C
Requires: libtiffxx5 = %version-%release

%description -n libtiff5
This package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

%description utils
This package contains simple client programs for accessing
the tiff functions.

%description -n tiffgt
This package contains tiffgt - a TIFF file display program.

%description devel
This package contains the header files for developing programs which
will manipulate TIFF format image files using the tiff library.

%description devel-static
This package contains static %name library.

%description -n libtiffxx5
This package contains TIFF I/O C++ shared library

%description -n libtiffxx-devel
This package contains TIFF I/O C++ development library and header files.

%prep
%setup -n %name-%version-%release
:>port/dummy.c

cd libtiff
cat > libtiff.sym << EOF
TIFFFaxBlackCodes
TIFFFaxBlackTable
TIFFFaxMainTable
TIFFFaxWhiteCodes
TIFFFaxWhiteTable
_TIFFCheckMalloc
_TIFFFax3fillruns
_TIFFMultiply32
_TIFFRewriteField
_TIFFGetExifFields
_TIFFClampDoubleToFloat
_TIFFFillStriles
TIFFFlushData1
_TIFFGetFields
_TIFFMergeFields
_TIFFSeekOK
_TIFFClampDoubleToUInt32
display_sRGB
EOF
sed -n 's/^extern[^)]\+[[:space:]]\*\?\([^[:space:]*()]\+\)[[:space:]]*(.*/\1/p' \
	tiffio.h >> libtiff.sym
sort -u -o libtiff.sym{,}
cat > libtiff.map << EOF
{
 global:
$(sed 's/.*/  &;/' libtiff.sym)
 local:
  *;
};
EOF
rm libtiff.sym

%build
%autoreconf
%define docdir %_docdir/%name-%version
%configure --with-docdir=%docdir --enable-ld-version-script \
	%{subst_enable static} %{subst_enable cxx}
%make_build X_PRE_LIBS= GLUT_CFLAGS= GLUT_CFLAGS= GLUT_LIBS='-lglut -lGL' \
	GLU_CFLAGS= GLU_LIBS= GL_CFLAGS= GL_LIBS=

%install
%makeinstall_std
xz -9 %buildroot%docdir/ChangeLog

%check
%make_build -k check

%files -n libtiff5
%_libdir/%name.so.?*
%dir %docdir
%docdir/[A-Z]*

%files utils
%_bindir/*
%_man1dir/*.*
%exclude %_bindir/tiffgt
%exclude %_man1dir/tiffgt.*

%files -n tiffgt
%_bindir/tiffgt
%_man1dir/tiffgt.*

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/*.h
%_man3dir/*.*
%dir %docdir
%docdir/html

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%if_enabled cxx
%files -n libtiffxx5
%_libdir/libtiffxx.so.*

%files -n libtiffxx-devel
%_libdir/libtiffxx.so
%_includedir/*.hxx
%endif

%changelog
* Sun Dec 18 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.4.0-alt2
- Applied SUSE patches (fixed tiff-CVE-2022-2056, CVE-2022-2057, CVE-2022-2058,
  CVE-2022-2519, CVE-2022-2520, CVE-2022-2521, CVE-2022-3597, CVE-2022-3598,
  CVE-2022-3599, CVE-2022-3626, CVE-2022-3627, CVE-2022-3970 and
  CVE-2022-34526) (closes #44499).

* Tue May 31 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.4.0-alt1
- Updated to v4.4.0.
- Dropped removed symbols from libtiff.sym.

* Mon Nov 29 2021 Vitaly Chikunov <vt@altlinux.org> 4.3.0-alt2
- Rebuilt with libdeflate support.

* Wed Sep 15 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.3.0-alt1
- Updated to v4.3.0.

* Fri Dec 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.2.0-alt1
- Updated to v4.2.0 (fixed CVE-2020-35521, CVE-2020-35522, CVE-2020-35523 and
  CVE-2020-35524).

* Thu Nov 14 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.1.0-alt1
- Updated to 4.1.0 (fixed CVE-2019-17546).
- Dropped tiff-CVE-2018-12900.patch.

* Tue Jun 04 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.10.0.93.91480d3d-alt1
- Updated to v4.0.10-93-g91480d3d.

* Tue Apr 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.10.0.57.f9fc01c3-alt1
- Updated to v4.0.10-57-gf9fc01c3 (ALT #36575, #34677).
- Applied SUSE patches:
  + tiff-4.0.3-seek.patch;
  + tiff-4.0.3-compress-warning.patch;
  + tiff-CVE-2018-12900.patch.
- Built with support of:
  + libjbig;
  + libwebp;
  + libzstd.
- Fixes:
  + CVE-2012-4564 Zero size buffer exploit in ppm2tiff;
  + CVE-2013-1960 Heap-based buffer overflow in the t2p_process_jpeg_strip();
  + CVE-2013-4232 Use-after-free vulnerability in the t2p_readwrite_pdf_image();
  + CVE-2013-4243 Heap-based buffer overflow in the readgifimage();
  + CVE-2013-4244 DoS or possible RCE via crafted GIF image;
  + CVE-2014-8127 Out-of-bounds read with malformed TIFF image in multiple tool;
  + CVE-2014-8129 Out-of-bounds read/write with malformed TIFF image in tiff2pdf;
  + CVE-2014-8130 Divide-by-zero error in _TIFFmalloc();
  + CVE-2014-9330 Integer overflow in tif_packbits.c in bmp2tif;
  + CVE-2015-8870 Integer overflow in tools/bmp2tiff.c (DoS or information leak);
  + CVE-2018-5360 Heap-based buffer overflow in the ReadTIFFImage().

* Sun Sep 23 2012 Dmitry V. Levin <ldv@altlinux.org> 4.0.3-alt1
- Updated to Release-v4-0-3.

* Sun Sep 02 2012 Dmitry V. Levin <ldv@altlinux.org> 4.0.2-alt2
- Updated to Release-v4-0-2-21-g8520941.
- Renamed: libtiff -> libtiff5, libtiffxx -> libtiffxx5.

* Mon Aug 27 2012 Dmitry V. Levin <ldv@altlinux.org> 3.9.6-alt3
- Updated to Release-v3-9-6-8-g0f67777
  (fixes CVE-2012-2113 CVE-2012-2088 CVE-2012-3401).

* Mon May 21 2012 Dmitry V. Levin <ldv@altlinux.org> 3.9.6-alt2
- Fixed build with ld --no-copy-dt-needed-entries.

* Sun Apr 08 2012 Dmitry V. Levin <ldv@altlinux.org> 3.9.6-alt1
- Updated to Release-v3-9-6-1-gc8ae292 (fixes CVE-2012-1173).

* Fri Jul 15 2011 Dmitry V. Levin <ldv@altlinux.org> 3.9.5-alt2
- Packaged libtiffxx (closes #25913).

* Wed Apr 13 2011 Dmitry V. Levin <ldv@altlinux.org> 3.9.5-alt1
- Updated to Release-v3-9-5 (fixes CVE-2011-1167).

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 3.9.4-alt5
- Updated to Release-v3-9-4-52-ga97ddb9
  (fixes CVE-2010-3087 CVE-2010-2595 CVE-2011-0192).

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 3.9.4-alt4
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 3.9.4-alt3
- Rebuilt for soname set-versions.

* Sun Jul 11 2010 Dmitry V. Levin <ldv@altlinux.org> 3.9.4-alt2
- Updated to Release-v3-9-4-20-g52cc6cb.
- Exported 6 more symbols needed by libfaxserver.

* Tue Jul 06 2010 Dmitry V. Levin <ldv@altlinux.org> 3.9.4-alt1
- Updated to Release-v3-9-4-15-gc603c15 (closes: #22115).
- Merged patches from Debian and Fedora libtiff packages.
- Restricted list of global symbols exported by the library.

* Wed Jul 15 2009 Dmitry V. Levin <ldv@altlinux.org> 3.8.2-alt5
- tiff2rgba, rgb2ycbcr: Fixed potential integer overflows in
  buffer size calculations (CVE-2009-2347; closes: #20774).

* Tue Jun 23 2009 Dmitry V. Levin <ldv@altlinux.org> 3.8.2-alt4
- Backported fix for buffer underflow bug in LZWDecodeCompat (closes: #20528).

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3.8.2-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sun Aug 31 2008 Dmitry V. Levin <ldv@altlinux.org> 3.8.2-alt2
- Applied patches from Drew Yao of Apple Product Security to fix
  potential buffer underflow in the LZW decoder (CVE-2008-2327).

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 3.8.2-alt1
- Updated to 3.8.2.
- Imported patches from Debian and FC.
- Updated build dependencies.

* Tue Oct 25 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.4-alt1
- Updated to 3.7.4.
- Updated patches.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.2-alt5
- Replaced my quick fix with upstream fix.

* Thu May 05 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.2-alt4
- Fixed one more potential heap overflow bug.

* Sun Apr 03 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.2-alt3
- Packaged tiffgt utility in separate subpackage (#6391).

* Thu Mar 24 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.2-alt2
- Backported fix for alpha channel handling in tiff2pdf.

* Wed Mar 16 2005 Dmitry V. Levin <ldv@altlinux.org> 3.7.2-alt1
- Updated to 3.7.2 release.
- Removed merged upstream patches.

* Fri Dec 24 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.1-alt3
- Fixed regression in TIFFRGBAImageBegin.

* Wed Dec 22 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.1-alt2
- Fixed potential crash in tiffdump(1).

* Tue Dec 21 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.1-alt1
- Updated to 3.7.1 release.
- Removed merged upstream patches.

* Mon Oct 25 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt2
- Check for invalid YCbCr subsampling.
- tiffset(1): minor fixes.

* Sat Oct 16 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0 release.

* Tue Oct 12 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt0.3
- Updated to cvs snapshot 20041011.
- Fixed regression introduced in 3.6.1-alt4.

* Mon Oct 11 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt0.2
- Updated to cvs snapshot 20041010.
- Removed merged upstream patches.

* Sun Oct 03 2004 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt0.1
- Updated to 3.7.0beta2.
- Reviewed patches again, since most of them are already applied.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt4
- Fixed numerous problems related to memory management.

* Mon Sep 20 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt3
- Backported upstream fixes for several buffer overrun bugs,
  reported by Chris Evans.

* Sun Sep 19 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.1-alt2
- Fixed issues which cause compilation warnings.

* Wed Sep 15 2004 Alexey Tourbin <at@altlinux.ru> 3.6.1-alt1
- 3.5.7 -> 3.6.1
- changed SONAME to reflect ABI changes (debian bug #236247)
- enabled LZW compression (%name-lzw-compression-kit-1.5)
- enforced strict dependencies between subpackages
- removed obsolete patches
- reworked build and install scriplets
- static library not packaged by default

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt4
- fix building in hasher

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt3
- fix fax2tiff crash

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt2
- Rebuild with gcc3

* Sat Aug 24 2002 Rider <rider@altlinux.ru> 3.5.7-alt1
- 3.5.7
- patches from RedHat

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 3.5.5-ipl3mdk
- rebuild

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 3.5.5-ipl2mdk
- Fixed config and install.
- Split into %name, %name-utils and %name-devel.

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.5-ipl1mdk
- RE adaptions.

* Mon Jun 26 2000 Alexandre Dussart <adussart@mandrakesoft.com> 3.5.5-1mdk
- 3.5.5
- Removed obsolete patch(check for libc6).
- Rewrittent some spec section to be more generic.
- Updated shlib patch.
- Removed LIBVER define.

* Tue Apr 18 2000 Warly <warly@linux-mandrake.com> 3.4-10mdk
- New group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP check/build
- Use good macro (old one may have bziped whole dirs)
- defattr

* Mon Jul 12 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip manpages

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Wed Jan 13 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against fixed jpeg libs (libjpeg-6b)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- new version to replace the one from libgr
- patched for glibc
- added shlib support
