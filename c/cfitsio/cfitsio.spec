
Name: cfitsio
Version: 3.280
Release: alt1
%define sversion %(echo %version | tr -d .)

Group: System/Libraries
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran

Url: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/

Source: ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/%name-%version.tar.gz
Patch0: cfitsio-3.280-autotools.patch
Patch1: cfitsio-3.280-alt-pkgconfig.patch

BuildRequires: flex gcc-c++ gcc-fortran glibc-devel

%description
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data format.
CFITSIO simplifies the task of writing software that deals with FITS
files by providing an easy to use set of high-level routines that insulate
the programmer from the internal complexities of the FITS file format.
At the same time, CFITSIO provides many advanced features that have made
it the most widely used FITS file programming interface in the astronomical
community.

%package -n lib%name
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: System/Libraries
%description -n lib%name
CFITSIO is a library of C and Fortran subroutines for reading and
writing data files in FITS (Flexible Image Transport System) data
format.  CFITSIO simplifies the task of writing software that deals
with FITS files by providing an easy to use set of high-level routines
that insulate the programmer from the internal complexities of the
FITS file format.  At the same time, CFITSIO provides many advanced
features that have made it the most widely used FITS file programming
interface in the astronomical community.  This package contains the
shared library required by prgrams that use the cfits library.

%package -n lib%name-devel
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: Development/C
Requires: lib%name = %version-%release
Provides: fitsio-devel = %version-%release
Provides: %name-devel = %version-%release
%description -n lib%name-devel
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

%package -n lib%name-devel-static
License: BSD-like
Summary: Library for accessing files in FITS format for C and Fortran
Group: Development/C
Requires: lib%name-devel = %version-%release
%description -n lib%name-devel-static
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
%setup -q
%patch0 -p0
%patch1 -p0
%autoreconf

%build
%configure --disable-static --enable-shared
%make_build

%install
install -d %buildroot/{%_libdir,%_includedir}
%makeinstall CFITSIO_LIB=%buildroot/%_libdir CFITSIO_INCLUDE=%buildroot/%_includedir


%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.3*

%files -n lib%name-devel
%_libdir/*.so
#%_libdir/*.la
%_includedir/*
%_libdir/pkgconfig/*

#%files -n lib%name-devel-static
#%_libdir/*.a

%changelog
* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 3.280-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 3.210-alt2
- rebuilt

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 3.210-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 3.100-alt1
- initial specfile

