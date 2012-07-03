Name: libtiff
Version: 3.9.6
Release: alt2

Summary: A library of functions for manipulating TIFF format image files
License: BSD-style
Group: System/Libraries
Url: http://www.remotesensing.org/libtiff/

# git://git.altlinux.org/gears/l/libtiff
Source: %name-%version-%release.tar

%def_disable static
%def_enable cxx

# Automatically added by buildreq on Tue Feb 08 2011
BuildRequires: gcc-c++ libSM-devel libXi-devel libXmu-devel libfreeglut-devel libjpeg-devel zlib-devel

%package utils
Summary: Programs for manipulating TIFF format image files
Group: Graphics
Requires: %name = %version-%release

%package -n tiffgt
Summary: Program for viewing TIFF format image files
Group: Graphics
Requires: %name = %version-%release

%package devel
Summary: Development files for programs which will use the tiff library
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static tiff library
Group: Development/C
Requires: %name-devel = %version-%release

%package -n libtiffxx
Summary: TIFF I/O C++ shared library
Group: System/Libraries
Requires: %name = %version-%release

%package -n libtiffxx-devel
Summary: TIFF I/O C++ development library and header files
Group: Development/C
Requires: libtiffxx = %version-%release

%description
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

%description -n libtiffxx
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
_TIFFDataSize
_TIFFFax3fillruns
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
./autogen.sh
%define docdir %_docdir/%name-%version
%configure --with-docdir=%docdir --enable-ld-version-script \
	%{subst_enable static} %{subst_enable cxx}
%make_build X_PRE_LIBS= GLUT_CFLAGS= GLUT_CFLAGS= GLUT_LIBS='-lglut -lGL' \
	GLU_CFLAGS= GLU_LIBS= GL_CFLAGS= GL_LIBS=

%install
%makeinstall_std
bzip2 -9 %buildroot%docdir/ChangeLog

%check
%make_build -k check

%files
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
%files -n libtiffxx
%_libdir/libtiffxx.so.*

%files -n libtiffxx-devel
%_libdir/libtiffxx.so
%_includedir/*.hxx
%endif

%changelog
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
