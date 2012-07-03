%define _optlevel s
%define beta %nil
%define libsover 6

%define rname OpenEXR 
Name: openexr
Version: 1.6.1
Release: alt7

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: Modified BSD
URL: http://www.openexr.org/

Requires: libilmimf%libsover = %version-%release
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release
Provides: %name-utils = %version-%release
Obsoletes: %name-utils < %version-%release

Source: %name-%version%beta.tar
Patch1: OpenEXR-1.2.2-zlib.patch
Patch2: OpenEXR-1.2.2-forwardfriend.patch
Patch3: openexr-1.4.0-alt-fix-linking.patch
Patch4: openexr-1.6.1-alt-gcc43.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libstdc++-devel pkg-config
#BuildRequires: gcc-c++ glibc-devel-static ilmbase-devel zlib-devel
BuildRequires: gcc-c++ glibc-devel ilmbase-devel zlib-devel

%description
OpenEXR is an image file format and library developed by Industrial Light
& Magic, and later released to the public. It provides support for high
dynamic range and a 16-bit floating point "half" data type which is
compatible with the half data type in the Cg programming language.


%package -n %name%libsover-common
Group: System/Configuration/Other
Summary: Common empty package for %name
%description -n %name%libsover-common
Common empty package for %name

%package -n libilmimf%libsover
Group: System/Libraries
Summary: libIlmImf %rname library
Requires: %name%libsover-common = %version-%release
Conflicts: openexr <= 1.6.1-alt1
%description -n libilmimf%libsover
libIlmImf %rname library

%package devel
Summary: Headers for developing programs that will use %rname
Group: Development/Other
Requires: %name%libsover-common = %version-%release
Requires: ilmbase-devel
#
%description devel
This package contains the static libraries and header files needed for
developing applications with %rname

%prep
%setup -q -n %name-%version
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
%patch4 -p1

#autoreconf
./bootstrap ||:


%build
%configure \
  --enable-shared \
  --disable-static \
  --enable-dependency-tracking \
  --enable-imfexamples \
  --disable-ilmbasetest

%make_build


%install
%make DESTDIR=%buildroot install
rm -rf ./installed-docs
ln -sf %buildroot/%_docdir/%rname-%version ./installed-docs



%files -n %name%libsover-common

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/*

%files -n libilmimf%libsover
%_libdir/libIlmImf.so.*

%files devel
%doc AUTHORS ChangeLog COPYING installed-docs/*
%_includedir/%rname
%_libdir/*.so
%_libdir/pkgconfig/*
%_datadir/aclocal/%name.m4


%changelog
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

