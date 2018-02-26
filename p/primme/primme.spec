%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.1.1
Name: primme
Version: 1.1
Release: alt10
Summary: PReconditioned Iterative MultiMethod Eigensolver
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.cs.wm.edu/~andreas/software/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cs.wm.edu/~andreas/software/primme_v1.1.tar.gz
Source1: http://www.cs.wm.edu/~andreas/software/doc.pdf

BuildPreReq: liblapack-devel libhypre-devel
BuildPreReq: %mpiimpl-devel chrpath

%description
PRIMME finds a number of eigenvalues and their corresponding eigenvectors of a 
real symmetric, or complex hermitian matrix A. Largest, smallest and interior 
eigenvalues are supported. Preconditioning can be used to accelarate
convergence.

PRIMME is written in C, but a complete Fortran77 interface is provided.

%package -n lib%name
Summary: Shared libraries of PRIMME
Group: System/Libraries

%description -n lib%name
PRIMME finds a number of eigenvalues and their corresponding eigenvectors of a 
real symmetric, or complex hermitian matrix A. Largest, smallest and interior 
eigenvalues are supported. Preconditioning can be used to accelarate
convergence.

This package contains shared libraries of PRIMME.

%package -n lib%name-devel
Summary: Development files of PRIMME
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
PRIMME finds a number of eigenvalues and their corresponding eigenvectors of a 
real symmetric, or complex hermitian matrix A. Largest, smallest and interior 
eigenvalues are supported. Preconditioning can be used to accelarate
convergence.

This package contains development files of PRIMME.

%package -n lib%name-devel-static
Summary: Static libraries of PRIMME
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
PRIMME finds a number of eigenvalues and their corresponding eigenvectors of a 
real symmetric, or complex hermitian matrix A. Largest, smallest and interior 
eigenvalues are supported. Preconditioning can be used to accelarate
convergence.

This package contains static libraries of PRIMME.

%package examples
Summary: Examples for PRIMME
Group: Development/Documentation
Requires: libhypre-devel

%description examples
PRIMME finds a number of eigenvalues and their corresponding eigenvectors of a 
real symmetric, or complex hermitian matrix A. Largest, smallest and interior 
eigenvalues are supported. Preconditioning can be used to accelarate
convergence.

This package contains examples for PRIMME.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%make lib libd libz TOP=$PWD
%make all TOP=$PWD MPIDIR=%mpidir

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_libdir/%name-%version/examples

install -m644 *.a %buildroot%_libdir
install -p -m644 PRIMMESRC/COMMONSRC/*.h \
	PRIMMESRC/DSRC/*.h PRIMMESRC/ZSRC/*.h \
	%buildroot%_includedir
rm -f DTEST/*.o ZTEST/*.o
cp -fR DTEST ZTEST %buildroot%_libdir/%name-%version/examples/

# shared libraries

pushd %buildroot%_libdir
for i in libprimme libdprimme libzprimme; do
	mpicc -shared -Wl,--whole-archive $i.a -Wl,--no-whole-archive \
		-L. $ADDLIB -llapack -lgoto2 -Wl,-rpath,%mpidir/lib \
		-Wl,-soname,$i.so.%somver -o $i.so.%sover -Wl,-z,defs
	ln -s $i.so.%sover $i.so.%somver
	ln -s $i.so.%somver $i.so
	#chrpath -r %mpidir/lib $i.so
	ADDLIB="-lprimme"
done
popd

%files
%doc COPYING.txt readme.txt doc.pdf
%dir %_libdir/%name-%version

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files examples
%dir %_libdir/%name-%version
%_libdir/%name-%version/examples

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt10
- Rebuilt witht OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt9
- Fixed RPATH

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt8
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt7
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt6
- Rebuilt for debuginfo

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt5
- Fixed overlinking of libraries

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4
- Rebuilt with Hypre 2.6.0b

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added shared libraries

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Rebuild with fixed Hypre

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

