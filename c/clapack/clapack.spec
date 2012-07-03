%define sover 0

Name: clapack
Version: 3.2.1
Release: alt1
Summary: C version of LAPACK
License: BSD
Group: Sciences/Mathematics
Url: http://www.netlib.org/clapack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: make.inc

BuildPreReq: libgotoblas-devel liblapack-devel libxblas-devel

%description
The CLAPACK library was built using a Fortran to C conversion utility
called f2c.  The entire Fortran 77 LAPACK library is run through f2c to
obtain C code, and then modified to improve readability.  CLAPACK's goal
is to provide LAPACK for someone who does not have access to a Fortran
compiler.

%package -n lib%name
Summary: Shared library of CLAPACK
Group: System/Libraries

%description -n lib%name
The CLAPACK library was built using a Fortran to C conversion utility
called f2c.  The entire Fortran 77 LAPACK library is run through f2c to
obtain C code, and then modified to improve readability.  CLAPACK's goal
is to provide LAPACK for someone who does not have access to a Fortran
compiler.

This package contains shared library of CLAPACK.

%package -n lib%name-devel
Summary: Development files of CLAPACK
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: libf2c-ng-devel

%description -n lib%name-devel
The CLAPACK library was built using a Fortran to C conversion utility
called f2c.  The entire Fortran 77 LAPACK library is run through f2c to
obtain C code, and then modified to improve readability.  CLAPACK's goal
is to provide LAPACK for someone who does not have access to a Fortran
compiler.

This package contains development files of CLAPACK.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build f2clib

%make_build -C INSTALL
%make_build -C SRC

gcc -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-Wl,-soname,lib%name.so.%sover -o lib%name.so.%sover \
	F2CLIBS/libf2c.a -lgoto2 -lxblas -lm

%install
install -d %buildroot%_includedir
install -p -m644 INCLUDE/* BLAS/WRAP/*.h %buildroot%_includedir

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%files -n lib%name
%doc COPYING
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Dec 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus

