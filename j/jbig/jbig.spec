Name: jbig
Version: 2.0
Release: alt2

# API change in version 1.6: jbg_enc_options(): parameter l0 changed type
# API change in version 1.5: struct jbg_enc_state: new member yd1
%define sover 1.6

Summary: JBIG-KIT lossless image compression library
License: GPL
Group: Graphics

Url: http://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source: jbigkit-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%package -n libjbig
Summary: JBIG-KIT lossless image compression library (shared library)
Group: System/Libraries

%package -n libjbig-devel
Summary: JBIG-KIT lossless image compression library (header files)
Group: Development/C
Requires: libjbig = %version-%release

%package -n libjbig-devel-static
Summary: JBIG-KIT lossless image compression library (static library)
Group: Development/C
Requires: libjbig-devel = %version-%release

%package utils
Summary: JBIG-KIT lossless image compression utilities
Group: Graphics
Requires: libjbig = %version-%release
Provides: jbigkit = %version
Obsoletes: jbigkit <= %version

%description
JBIG is a highly effective lossless compression algorithm for bi-level
images (one bit per pixel), which is particularly suitable for scanned
document pages.

%description -n libjbig
JBIG is a highly effective lossless compression algorithm for bi-level
images (one bit per pixel), which is particularly suitable for scanned
document pages.

This package is required for libjbig-based programs.

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
%setup -n jbigkit

%build
# First, build shared library.
pushd libjbig
%make_build libjbig.a CFLAGS='%optflags %optflags_shared'
gcc -shared -o libjbig.so.%sover -Wl,-soname=libjbig.so.%sover `ar t libjbig.a`
ln -snf libjbig.so.%sover libjbig.so
make clean
popd

# Second, build all the rest.
%make_build CCFLAGS='%optflags'

LD_LIBRARY_PATH=$PWD/libjbig make test

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_man1dir}
install -p -m755 pbmtools/{jbgtopbm,pbmtojbg} %buildroot%_bindir/
install -p -m644 pbmtools/*.1 %buildroot%_man1dir/
install -p -m644 libjbig/jbig{,_ar}.h %buildroot%_includedir/
cp -a libjbig/libjbig.so* %buildroot%_libdir/
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
%make_build -k test

%files -n libjbig
%_libdir/libjbig.so.%sover
%dir %pkgdocdir
%pkgdocdir/ANNOUNCE
%pkgdocdir/CHANGES
%pkgdocdir/README

%files -n libjbig-devel
%_libdir/libjbig.so
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
