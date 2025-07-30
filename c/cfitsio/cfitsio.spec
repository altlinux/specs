%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define rname cfitsio
%define sover 10
%define libname libcfitsio%sover
%define devame libcfitsio-devel

Name: cfitsio
Version: 4.6.2
Release: alt2
%define sversion %(echo %version | tr -d .)

Group: System/Libraries
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran

Url: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/

Source: %rname-%version.tar

BuildRequires: flex gcc-c++ gcc-fortran glibc-devel zlib-devel bzlib-devel
BuildRequires: chrpath

%description
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data format.
CFITSIO simplifies the task of writing software that deals with FITS
files by providing an easy to use set of high-level routines that insulate
the programmer from the internal complexities of the FITS file format.
At the same time, CFITSIO provides many advanced features that have made
it the most widely used FITS file programming interface in the astronomical
community.

%package -n %libname
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: System/Libraries
%description -n %libname
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data
format.  CFITSIO simplifies the task of writing software that deals
with FITS files by providing an easy to use set of high-level routines
that insulate the programmer from the internal complexities of the
FITS file format.  At the same time, CFITSIO provides many advanced
features that have made it the most widely used FITS file programming
interface in the astronomical community.  This package contains the
shared library required by prgrams that use the cfits library.

%package -n %devame
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: Development/C
Requires: %libname = %version-%release
Provides: fitsio-devel = %version-%release
Provides: %name-devel = %version-%release
%description -n %devame
  CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data format.
CFITSIO simplifies the task of writing software that deals with FITS
files by providing an easy to use set of high-level routines that insulate
the programmer from the internal complexities of the FITS file format.
At the same time, CFITSIO provides many advanced features that have made
it the most widely used FITS file programming interface in the astronomical
community.
  This package contains the headers required for compiling software that uses
the cfits library.

%prep
%setup -n %rname-%version

%build
%configure --disable-static --enable-shared --enable-reentrant --with-bzip2
%make_build

%install
%makeinstall_std

chrpath -d %buildroot%_bindir/*

%files
%_bindir/f*

%files -n %libname
%_libdir/*.so.%sover
%_libdir/*.so.*

%files -n %devame
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*

%changelog
* Wed Jul 30 2025 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- don't package contlicting utilities (closes: 55407)

* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 4.6.2-alt1
- NMU: new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 3.490-alt2
- fix to build with LTO

* Wed May 26 2021 Sergey V Turchin <zerg@altlinux.org> 3.490-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 3.380-alt2
- fix requires

* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 3.380-alt1
- new version

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

