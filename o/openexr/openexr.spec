%define libsover 24

%define rname OpenEXR
Name: openexr
Version: 2.3.0
Release: alt2

%define common %name%libsover-common
%define libilmimf libilmimf%libsover
%define libilmimfutil libilmimfutil%libsover

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: BSD
URL: http://www.openexr.org/

Requires: %libilmimf = %version-%release
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release
Provides: %name-utils = %version-%release
Obsoletes: %name-utils < %version-%release

Source: %name-%version.tar
# FC
Patch1: openexr-2.3.0-bigendian.patch
Patch2: openexr-2.3.0-tests.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libstdc++-devel pkg-config
#BuildRequires: gcc-c++ glibc-devel-static ilmbase-devel zlib-devel
BuildRequires: gcc-c++ glibc-devel ilmbase-devel zlib-devel
BuildRequires: cmake kde-common-devel

%description
OpenEXR is an image file format and library developed by Industrial Light
& Magic, and later released to the public. It provides support for high
dynamic range and a 16-bit floating point "half" data type which is
compatible with the half data type in the Cg programming language.


%package -n %common
Group: System/Configuration/Other
Summary: Common empty package for %name
%description -n %common
Common empty package for %name

%package -n %libilmimf
Group: System/Libraries
Summary: libIlmImf %rname library
Requires: %common = %version-%release
Conflicts: openexr <= 1.6.1-alt1
%description -n %libilmimf
libIlmImf %rname library

%package -n %libilmimfutil
Group: System/Libraries
Summary: libIlmImfUtil %rname library
Requires: %common = %version-%release
Conflicts: openexr <= 1.6.1-alt1
%description -n %libilmimfutil
libIlmImfUtil %rname library

%package devel
Summary: Headers for developing programs that will use %rname
Group: Development/Other
Requires: %common = %version-%release
Requires: ilmbase-devel
#
%description devel
This package contains the static libraries and header files needed for
developing applications with %rname

%prep
%setup -q -n %name-%version
%patch1 -p2
%patch2 -p2
%ifarch %e2k
# e2k has MMX/SSE but 2.2.0+'s asm needs to be ported
%add_optflags -U__SSE2__ -U__SSE4_1__
%endif

%build
%configure \
    --disable-static \
    #
%make_build

%install
%makeinstall_std


%files -n %common

%files
%_bindir/*

%files -n %libilmimf
%doc AUTHORS ChangeLog PATENTS LICENSE README*
%_libdir/libIlmImf-*.so.%libsover
%_libdir/libIlmImf-*.so.%libsover.*
%files -n %libilmimfutil
%doc AUTHORS ChangeLog PATENTS LICENSE README*
%_libdir/libIlmImfUtil-*.so.%libsover
%_libdir/libIlmImfUtil-*.so.%libsover.*

%files devel
%doc doc/*.pdf
%_includedir/%rname
%_libdir/lib*.so
%_libdir/pkgconfig/*
#%_datadir/aclocal/%name.m4


%changelog
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

