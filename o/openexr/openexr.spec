%define rname OpenEXR
%define libsover 30
Name: openexr
Version: 3.1.5
Release: alt2

%define _cmake__builddir BUILD
%define common %name%libsover-common
%define libopenexr libopenexr%libsover
%define libiex libiex%libsover
%define libilmthread libilmthread%libsover
%define libopenexrcore libopenexrcore%libsover
%define libopenexrutil libopenexrutil%libsover

Summary: A high-dynamic-range image file library
License: BSD-3-Clause
Group: System/Libraries
URL: http://www.openexr.org/

Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release
Provides: %name-utils = %version-%release
Obsoletes: %name-utils < %version-%release

Source: %name-%version.tar

BuildRequires: gcc-c++ glibc-devel zlib-devel
BuildRequires: imath-devel
BuildRequires: python3-module-imath
BuildRequires: cmake

%define descr The OpenEXR project provides the specification and reference \
implementation of the EXR file format, the professional-grade \
image storage format of the motion picture industry. \
\
The purpose of EXR format is to accurately and efficiently represent \
high-dynamic-range scene-linear image data and associated metadata, \
with strong support for multi-part, multi-channel use cases. \
\
OpenEXR is widely used in host application software where accuracy is critical, \
such as photorealistic rendering, texture access, image compositing, \
deep compositing, and DI.

%description
%descr

%package -n %common
Group: System/Configuration/Other
Summary: Common empty package for %name
BuildArch: noarch

%description -n %common
Common empty package for %name

%package -n %libopenexr
Summary: %rname library
Group: System/Libraries

%description -n %libopenexr
%descr

%package devel
Summary: Headers for developing programs that will use OpenEXR
Group: Development/Other
Provides: ilmbase-devel = %version
Obsoletes: ilmbase-devel < %version
Requires: imath-devel
%description devel
%descr

This package contains the static libraries and header files needed for
developing applications with OpenEXR

%package -n %libiex
Summary: libIex %rname library
Group: System/Libraries

%description -n %libiex
%descr

%package -n %libilmthread
Summary: libIlmThread %rname library
Group: System/Libraries

%description -n %libilmthread
%descr

%package -n %libopenexrcore
Summary: libOpenEXRCore %rname library
Group: System/Libraries

%description -n %libopenexrcore
%descr

%package -n %libopenexrutil
Summary: libOpenEXRUtil %rname library
Group: System/Libraries

%description -n %libopenexrutil
%descr

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install
make -C BUILD install DESTDIR=%buildroot CMAKE_MODULE_PATH=%_includedir/Imath

%files -n %common
%doc *.md
%_docdir/%rname/examples

%files
%_bindir/*

%files -n %libopenexr
%_libdir/libOpenEXR-*.so.%libsover
%_libdir/libOpenEXR-*.so.%libsover.*

%files devel
%_libdir/lib*.so
%_includedir/OpenEXR/*
%_pkgconfigdir/OpenEXR.pc
%_libdir/cmake/OpenEXR/*.cmake

%files -n %libiex
%_libdir/libIex*.so.%libsover
%_libdir/libIex*.so.%libsover.*

%files -n %libilmthread
%_libdir/libIlmThread*.so.%libsover
%_libdir/libIlmThread*.so.%libsover.*

%files -n %libopenexrcore
%_libdir/libOpenEXRCore*.so.%libsover
%_libdir/libOpenEXRCore*.so.%libsover.*

%files -n %libopenexrutil
%_libdir/libOpenEXRUtil*.so.%libsover
%_libdir/libOpenEXRUtil*.so.%libsover.*

%changelog
* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 3.1.5-alt2
- fix conflicts

* Fri Feb 03 2023 Alexander Burmatov <thatman@altlinux.org> 3.1.5-alt1
- Updated to upstream version 3.1.5

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
