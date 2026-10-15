%define oname libjbig
%define sover 2.1

Name: %oname%sover
Version: 2.1
Release: alt3

Summary: JBIG-KIT lossless image compression library (legacy)

License: GPLv2+
Group: System/Legacy libraries
Url: http://www.cl.cam.ac.uk/~mgk25/jbigkit/

# Source-url: http://www.cl.cam.ac.uk/~mgk25/download/jbigkit-%version.tar.gz
Source: %name-%version.tar

Patch: jbigkit-2.1-shlib.patch
Patch1: jbigkit-2.0-warnings.patch
Patch2: jbigkit-ldflags.patch
# patch for coverity issues - backported from upstream
Patch3: jbigkit-covscan.patch

%description
This package contains legacy JBIG-KIT shared libraries libjbig.so.2.1
and libjbig85.so.2.1 for compatibility with already built programs.

%prep
%setup
%patch0 -p1 -b .shlib
%patch1 -p1 -b .warnings
# jbigkit: Partial Fedora build flags injection (bug #1548546)
%patch2 -p1 -b .ldflags
# covscan issues - backported from upstream
%patch3 -p1 -b .covscan

%build
%make_build CCFLAGS='%optflags'

%install
mkdir -p %buildroot%_libdir
install -p -m0755 libjbig/libjbig.so.%sover %buildroot%_libdir
install -p -m0755 libjbig/libjbig85.so.%sover %buildroot%_libdir

%check
LD_LIBRARY_PATH=$PWD/libjbig %make -k test

%files
%_libdir/libjbig.so.%sover
%_libdir/libjbig85.so.%sover

%changelog
* Tue Oct 13 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt3
- build legacy libjbig.so.2.1, libjbig85.so.2.1 only (jbig 2.2 has soname 2.2)

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
