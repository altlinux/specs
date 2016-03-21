
%define rname cfitsio

Name: cfitsio3
Version: 3.370
Release: alt2
%define sversion %(echo %version | tr -d .)

Group: System/Libraries
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran

Url: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/

Source: ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/%rname-%version.tar.gz
# SuSE
Patch1: cfitsio-zlib.patch
# FC
Patch5: cfitsio-pkgconfig.patch
# ALT
Patch10: cfitsio-3.360-autotools.patch
Patch11: cfitsio-3.350-alt-pkgconfig.patch
Patch12: cfitsio-3.360-soname.patch

BuildRequires: flex gcc-c++ gcc-fortran glibc-devel zlib-devel

%description
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data format.
CFITSIO simplifies the task of writing software that deals with FITS
files by providing an easy to use set of high-level routines that insulate
the programmer from the internal complexities of the FITS file format.
At the same time, CFITSIO provides many advanced features that have made
it the most widely used FITS file programming interface in the astronomical
community.

%package -n lib%rname
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: System/Libraries
%description -n lib%rname
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data
format.  CFITSIO simplifies the task of writing software that deals
with FITS files by providing an easy to use set of high-level routines
that insulate the programmer from the internal complexities of the
FITS file format.  At the same time, CFITSIO provides many advanced
features that have made it the most widely used FITS file programming
interface in the astronomical community.  This package contains the
shared library required by prgrams that use the cfits library.

%prep
%setup -qn %rname-%version
%patch1 -p1
%patch5 -p1
%patch10 -p0
#%patch11 -p0
%patch12 -p0
#autoreconf

%build
%configure --disable-static --enable-shared --enable-reentrant
%make_build shared
%make_build fpack
%make_build funpack

%install
install -d %buildroot/{%_bindir,%_libdir,%_includedir/%rname}
%make \
    LIBDIR=%_libdir \
    INCLUDEDIR=%_includedir/%rname \
    CFITSIO_LIB=%buildroot%_libdir \
    CFITSIO_INCLUDE=%buildroot%_includedir/%rname \
install
install -m755 f{,un}pack %buildroot/%_bindir/

%files -n lib%rname
%_libdir/*.so.3
%_libdir/*.so.3.*


%changelog
* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 3.370-alt2
- build only library

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 3.370-alt1
- new version

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 3.360-alt1
- new version

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 3.350-alt0.M70P.1
- built for M70P

* Mon Oct 07 2013 Sergey V Turchin <zerg@altlinux.org> 3.350-alt1
- new version

* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 3.280-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 3.210-alt2
- rebuilt

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 3.210-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 3.100-alt1
- initial specfile

