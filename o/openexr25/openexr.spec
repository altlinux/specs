%define rname OpenEXR
%define libsover 25
Name: openexr25
Version: 2.5.6
Release: alt5

%define _cmake__builddir BUILD
%define libilmimf libilmimf%libsover
%define libilmimfutil libilmimfutil%libsover

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: BSD-3-Clause
URL: http://www.openexr.org/

Requires: %libilmimf = %version-%release
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source: openexr-%version.tar
# upstream
Patch1: oss-fuzz.patch
Patch2000: openexr-e2k-simd.patch

BuildRequires: gcc-c++ glibc-devel ilmbase-devel zlib-devel
BuildRequires: cmake

%description
OpenEXR is an image file format and library developed by Industrial Light
& Magic, and later released to the public. It provides support for high
dynamic range and a 16-bit floating point "half" data type which is
compatible with the half data type in the Cg programming language.

%package -n %libilmimf
Group: System/Libraries
Summary: libIlmImf %rname library
Conflicts: openexr <= 1.6.1-alt1
%description -n %libilmimf
libIlmImf %rname library

%package -n %libilmimfutil
Group: System/Libraries
Summary: libIlmImfUtil %rname library
Conflicts: openexr <= 1.6.1-alt1
%description -n %libilmimfutil
libIlmImfUtil %rname library

%prep
%setup -q -n openexr-%version
%patch1 -p1
%ifarch %e2k
%patch2000 -p2
%endif

%build
%cmake
%cmake_build

%install
make -C BUILD install DESTDIR=%buildroot
rm -fr %buildroot%_bindir/
rm -fr %buildroot%_includedir/%rname/
rm -fr %buildroot%_libdir/cmake/%rname/
rm -fr %buildroot%_libdir/libIlmImf*.so
rm -fr %buildroot%_libdir/pkgconfig/%rname.pc
rm -fr %buildroot%doc/%rname/
rm -fr %buildroot%_defaultdocdir/%rname/

%files -n %libilmimf
%doc PATENTS README*
%_libdir/libIlmImf-*.so.%libsover
%_libdir/libIlmImf-*.so.%libsover.*
%files -n %libilmimfutil
%doc PATENTS README*
%_libdir/libIlmImfUtil-*.so.%libsover
%_libdir/libIlmImfUtil-*.so.%libsover.*

%changelog
* Fri Feb 03 2023 Alexander Burmatov <thatman@altlinux.org> 2.5.6-alt5
- create compatibility package

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 2.5.6-alt4
- add upstream fixes against oss-fuzz issues 28051,28055

* Mon Jun 21 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.5.6-alt3
- added SIMD patch for Elbrus

* Wed Jun 09 2021 Sergey V Turchin <zerg@altlinux.org> 2.5.6-alt2
- compatable with p9

* Thu May 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.5.6-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed May 26 2021 Sergey V Turchin <zerg@altlinux.org> 2.5.6-alt1
- new version

* Mon Oct 26 2020 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- new version

* Sat Sep 21 2019 Michael Shigorin <mike@altlinux.org> 2.3.0-alt2
- E2K: avoid SIMD for now (SSE asm needs to be ported)

* Fri Sep 20 2019 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt3
- fix to build with gcc8

* Thu Sep 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.2.0-alt2
- Security (Fixes: CVE-2017-9110, CVE-2017-9111, CVE-2017-9112,
  CVE-2017-9113, CVE-2017-9114, CVE-2017-9115, CVE-2017-9116)

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.2.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt7
- fix build requires

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt6
- rebuilt

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt5
- rebuilt

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt4
- rebuilt

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt3
- fix compile with new gcc
- remove deprecated macroses from specfile

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt2
- split lib* subpackages

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt1
- new version

* Mon May 14 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.0-alt1.a
- new version
- built with libfltk

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt4
- built without libfltk

* Mon May 15 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt3
- rebuilt with new gcc

* Tue Mar 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt2
- add patch for linking with zlib from FC

* Thu Aug 25 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt1
- new version
- split utils to separate package

* Mon Sep 27 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.1-alt1
- initial spec

