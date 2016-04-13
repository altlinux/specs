%define libsover 21

%define rname OpenEXR
Name: openexr21
Version: 2.1.0
Release: alt3.qa1

%define common %name-common
%define libilmimf libilmimf%libsover

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: BSD
URL: http://www.openexr.org/

Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source: openexr-%version.tar
# FC
Patch1: openexr-2.1.0-bigendian.patch
# ALT
Patch10: openexr-2.1.0-alt-build.patch
Patch11: openexr-2.1.0-alt-libdir.patch
Patch12: openexr-2.1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils libstdc++-devel pkg-config
#BuildRequires: gcc-c++ glibc-devel-static ilmbase-devel zlib-devel
BuildRequires: gcc-c++ glibc-devel ilmbase11-devel zlib-devel
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

%package devel
Summary: Headers for developing programs that will use %rname
Group: Development/Other
Requires: %common = %version-%release
Requires: ilmbase11-devel
#
%description devel
This package contains the static libraries and header files needed for
developing applications with %rname

%prep
%setup -q -n openexr-%version
%patch1 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%add_optflags -D_GLIBCXX_USE_CXX11_ABI=0

%Kcmake
%Kmake

%install
%Kinstall

# create compatibility symlinks
for f in %buildroot/%_libdir/lib*.so ; do
    fname=`basename $f`
    newname=`echo $fname | sed 's|-.*|.so|'`
    [ "$fname" == "$newname" ] \
	|| ln -s $fname %buildroot/%_libdir/$newname
done

mv %buildroot/%_docdir/%rname-%version %buildroot/%_docdir/%name-%version
install -m 0644 AUTHORS %buildroot/%_docdir/%name-%version/
install -m 0644 ChangeLog %buildroot/%_docdir/%name-%version/
install -m 0644 COPYING %buildroot/%_docdir/%name-%version/
install -m 0644 NEWS %buildroot/%_docdir/%name-%version/
install -m 0644 README %buildroot/%_docdir/%name-%version/

%files -n %common

%files -n %libilmimf
%_libdir/libIlmImf-*.so.%libsover
%_libdir/libIlmImf-*.so.%libsover.*

%files devel
%doc %_docdir/%name-%version/
%_includedir/%rname
%_libdir/lib*.so
%_libdir/pkgconfig/*
#%_datadir/aclocal/%name.m4


%changelog
* Wed Apr 13 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2.1.0-alt3.qa1
- Switched build to old CXX ABI.

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt3
- don't package utils

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- create compatibility package

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

