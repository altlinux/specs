%define scalar_type real

%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl
%define ldir %_libexecdir/petsc-%scalar_type

%define oname blopex
%define lname libBLOPEX
%define somver 0
%define sover %somver.1.0

Name: %oname-%scalar_type
Version: 1.1
Release: alt4.svn20101114
%if %scalar_type == real
Provides: %oname = %version-%release
Obsoletes: %oname < %version-%release
%endif
Summary: Block Locally Optimal Preconditioned Eigenvalue Xolvers
Group: Sciences/Mathematics
License: LGPL
URL: http://code.google.com/p/blopex/

# http://blopex.googlecode.com/svn/trunk/
Source: blopex_abstract.tar.gz
Source1: blopex_serial.tar.gz
Source2: BLOPEX.html
Source3: blopex_petsc.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: liblapack-goto-devel libpetsc-%scalar_type-devel
BuildPreReq: libtrilinos10-devel libamesos10-devel
BuildPreReq: libepetraext10-devel libifpack10-devel

%description
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

%package -n lib%oname
Summary: Shared library of BLOPEX
Group: System/Libraries

%description -n lib%oname
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains shared library of BLOPEX.

%package -n lib%oname-devel
Summary: Development files of BLOPEX
Group: Development/C
Requires: lib%oname = %version-%release
Conflicts: lib%oname-devel < %version-%release
Obsoletes: lib%oname-devel < %version-%release

%description -n lib%oname-devel
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains development files of BLOPEX.

%package -n lib%oname-devel-static
Summary: Static library of BLOPEX
Group: Development/C
Requires: lib%oname-devel = %version-%release
Conflicts: lib%oname-devel < %version-%release

%description -n lib%oname-devel-static
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains static library of BLOPEX.

%package -n lib%oname-petsc-%scalar_type-interface
Summary: BLOPEX interface library with PETSc (%scalar_type scalars)
Group: System/Libraries

%description -n lib%oname-petsc-%scalar_type-interface
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains BLOPEX interface library with PETSc.

%package -n lib%oname-petsc-%scalar_type-interface-devel
Summary: Development files of BLOPEX's PETSc interface (%scalar_type scalars)
Group: Development/C++
Requires: lib%oname-petsc-%scalar_type-interface = %version-%release

%description -n lib%oname-petsc-%scalar_type-interface-devel
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains development files of BLOPEX interface library with
PETSc.

%package -n %oname-petsc-%scalar_type-drivers
Summary: Test drivers for BLOPEX interface with PETSc (%scalar_type scalars)
Group: Sciences/Mathematics
Requires: lib%oname-petsc-%scalar_type-interface = %version-%release

%description -n %oname-petsc-%scalar_type-drivers
BLOPEX is a package, written in C, that at present includes only one
eigenxolver, Locally Optimal Block Preconditioned Conjugate Gradient Method
(LOBPCG). BLOPEX supports parallel MPI-based computations through an abstract
layer.

This package contains test drivers for BLOPEX interface library with
PETSc.

%prep
tar -xzf %SOURCE0
tar -xzf %SOURCE1
tar -xzf %SOURCE3
install %SOURCE2 .

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

pushd %{oname}_abstract
%make_build
popd
pushd %{oname}_serial
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/lib%oname
install -d %buildroot%ldir/bin
install -d %buildroot%ldir/include/%oname/petsc-interface

install -m755 %{oname}_serial/driver/serial_driver %buildroot%_bindir
install -m644 %{oname}_abstract/lib/*.a %buildroot%_libdir
for i in %{oname}_abstract/include/*.h %{oname}_abstract/utilities/*.h \
	$(find %{oname}_serial -name '*.h'); do
cp -f $i %buildroot%_includedir/lib%oname
done

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../%lname.a
gcc -shared * -llapack -lm \
	-Wl,-soname,%lname.so.%somver -o ../%lname.so.%sover
rm -f *
popd
rmdir tmp
ln -s %lname.so.%sover %lname.so.%somver
ln -s %lname.so.%somver %lname.so
popd

# interface with PETSc

pushd %{oname}_petsc
for i in . petsc-interface driver driver_fiedler
do
	rm -f $i/makefile
done
cp ../blopex_abstract/include/*.h petsc-interface/
source %_bindir/petsc-%scalar_type.sh

%make_build petsc_interface 
ADDLIB=-llapack
mpicxx -shared -o lib%oname-petsc-%scalar_type-interface.so.%sover \
	-Wl,-soname,lib%oname-petsc-%scalar_type-interface.so.%somver \
	petsc-interface/*.o \
	-L%buildroot%_libdir -lBLOPEX \
	$(pkg-config --libs petsc-%scalar_type) $ADDLIB
ln -s lib%oname-petsc-%scalar_type-interface.so.%sover \
	lib%oname-petsc-%scalar_type-interface.so.%somver
ln -s lib%oname-petsc-%scalar_type-interface.so.%somver \
	lib%oname-petsc-%scalar_type-interface.so

export BUILDROOTLIB=%buildroot%_libdir
#make_build driver
#make_build -C driver_diag driver_diag SCALAR_TYPE=%scalar_type
#make_build -C driver_fiedler

#for i in driver driver_diag driver_fiedler
#do
#	chrpath -r %mpidir/lib:%ldir/lib $i/$i
#	mv $i/$i %oname-petsc-$i
#done

install -m644 lib%oname-petsc-%scalar_type-interface.so.%sover \
	%buildroot%_libdir
ln -s lib%oname-petsc-%scalar_type-interface.so.%sover \
	%buildroot%_libdir/lib%oname-petsc-%scalar_type-interface.so.%somver
ln -s lib%oname-petsc-%scalar_type-interface.so.%somver \
	%buildroot%_libdir/lib%oname-petsc-%scalar_type-interface.so
install petsc-interface/*.h %buildroot%ldir/include/%oname/petsc-interface
#install -m755 %oname-petsc-driver* %buildroot%ldir/bin
popd

%if %scalar_type == real
%files
%_bindir/*

%files -n lib%oname
%_libdir/*.so.*
%exclude %_libdir/lib%oname-petsc-%scalar_type-interface.so.*

%files -n lib%oname-devel
%doc BLOPEX.html
%_libdir/*.so
%exclude %_libdir/lib%oname-petsc-%scalar_type-interface.so
%_includedir/*

#files -n lib%oname-devel-static
#_libdir/*.a
%endif

%files -n lib%oname-petsc-%scalar_type-interface
%_libdir/lib%oname-petsc-%scalar_type-interface.so.*

%files -n lib%oname-petsc-%scalar_type-interface-devel
%doc %{oname}_petsc/petsc-interface/*.c
%_libdir/lib%oname-petsc-%scalar_type-interface.so
%ldir/include/%oname/petsc-interface

#files -n %oname-petsc-%scalar_type-drivers
#doc %{oname}_petsc/driver*/*.c
#ldir/bin/*

# TODO: build driver_fortran, blopex_hypre

%changelog
* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4.svn20101114
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3.svn20101114
- Fixed RPATH

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.svn20101114
- Rebuilt with PETSc 3.2-p5

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20101114.2
- Rebuilt with PETSc interface

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20101114.1
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package
- Bootstrap (without PETSc interface)

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20101114
- Version 1.1

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709.5
- Rebuilt for debuginfo (stage 2)

* Mon Feb 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709.4
- Rebuilt for debuginfo (stage 1)

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709.2
- Fixed linking of libraries

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709.1
- Rebuilt with PETSc 3.1-p3

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100709
- New snapshot
- Added necessary headers for interface with PETSc

* Sun Jul 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100518.1
- Added interface with PETSc and some test drivers

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20100518
- Built from svn

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added shared library

* Sat Jun 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Fixed headers

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Rebuild with PIC

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

