%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define over 2.4
%define somver 2
%define sover %somver.5
Name: superlu_dist
Version: 3.1
Release: alt1
Summary: Solve a sparse linear system A*X=B for distributed memory
License: BSD-like
Group: Sciences/Mathematics
Url: http://acts.nersc.gov/superlu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %{name}_%version.tar.gz
Source1: superlu_sort_perm.c

BuildPreReq: libgotoblas-devel liblapack-devel
BuildPreReq: csh libparmetis-devel %mpiimpl-devel
#BuildPreReq: texlive-latex-base texlive-extra-utils
#BuildPreReq: doxygen graphviz ghostscript-utils

%description
SuperLU_DIST contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with static pivoting (GESP). 
Static pivoting is a technique that combines the numerical stability of
partial pivoting with the scalability of Cholesky (no pivoting),
to run accurately and efficiently on large numbers of processors. 

SuperLU_DIST is a parallel extension to the serial SuperLU library.
It is targeted for the distributed memory parallel machines.
SuperLU_DIST is implemented in ANSI C, and MPI for communications.
Currently, the LU factorization and triangular solution routines,
which are the most time-consuming part of the solution process,
are parallelized. The other routines, such as static pivoting and 
column preordering for sparsity are performed sequentially. 
This "alpha" release contains double-precision real and double-precision
complex data types.

%package -n lib%name
Summary: Shared library of SuperLU_DIST
Group: System/Libraries

%description -n lib%name
SuperLU_DIST contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with static pivoting (GESP). 
Static pivoting is a technique that combines the numerical stability of
partial pivoting with the scalability of Cholesky (no pivoting),
to run accurately and efficiently on large numbers of processors. 

SuperLU_DIST is a parallel extension to the serial SuperLU library.
It is targeted for the distributed memory parallel machines.
SuperLU_DIST is implemented in ANSI C, and MPI for communications.
Currently, the LU factorization and triangular solution routines,
which are the most time-consuming part of the solution process,
are parallelized. The other routines, such as static pivoting and 
column preordering for sparsity are performed sequentially. 
This "alpha" release contains double-precision real and double-precision
complex data types.

This package contains shared library of SuperLU_DIST.

%package -n lib%name-devel
Summary: Development files of SuperLU_DIST
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release
Requires: %mpiimpl-devel

%description -n lib%name-devel
SuperLU_DIST contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with static pivoting (GESP). 
Static pivoting is a technique that combines the numerical stability of
partial pivoting with the scalability of Cholesky (no pivoting),
to run accurately and efficiently on large numbers of processors. 

SuperLU_DIST is a parallel extension to the serial SuperLU library.
It is targeted for the distributed memory parallel machines.
SuperLU_DIST is implemented in ANSI C, and MPI for communications.
Currently, the LU factorization and triangular solution routines,
which are the most time-consuming part of the solution process,
are parallelized. The other routines, such as static pivoting and 
column preordering for sparsity are performed sequentially. 
This "alpha" release contains double-precision real and double-precision
complex data types.

This package contains development files of SuperLU_DIST.

%package -n lib%name-devel-doc
Summary: Documentation for SuperLU_DIST
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
SuperLU_DIST contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with static pivoting (GESP). 
Static pivoting is a technique that combines the numerical stability of
partial pivoting with the scalability of Cholesky (no pivoting),
to run accurately and efficiently on large numbers of processors. 

SuperLU_DIST is a parallel extension to the serial SuperLU library.
It is targeted for the distributed memory parallel machines.
SuperLU_DIST is implemented in ANSI C, and MPI for communications.
Currently, the LU factorization and triangular solution routines,
which are the most time-consuming part of the solution process,
are parallelized. The other routines, such as static pivoting and 
column preordering for sparsity are performed sequentially. 
This "alpha" release contains double-precision real and double-precision
complex data types.

This package contains documentation for SuperLU_DIST.

%package examples
Summary: Examples of using SuperLU_DIST
Group: Sciences/Mathematics

%description examples
SuperLU_DIST contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with static pivoting (GESP). 
Static pivoting is a technique that combines the numerical stability of
partial pivoting with the scalability of Cholesky (no pivoting),
to run accurately and efficiently on large numbers of processors. 

SuperLU_DIST is a parallel extension to the serial SuperLU library.
It is targeted for the distributed memory parallel machines.
SuperLU_DIST is implemented in ANSI C, and MPI for communications.
Currently, the LU factorization and triangular solution routines,
which are the most time-consuming part of the solution process,
are parallelized. The other routines, such as static pivoting and 
column preordering for sparsity are performed sequentially. 
This "alpha" release contains double-precision real and double-precision
complex data types.

This package contains examples of using SuperLU_DIST.

%prep
%setup

install -m644 %SOURCE1 SRC

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export HOME=$PWD
export MPIDIR=%mpidir
export PATH=$PATH:$MPIDIR/bin
mkdir -p lib
%make_build lib
#make_build install example
%make_build install
pushd FORTRAN
%make
popd
%make -C SRC superlu_sort_perm.o
%make -C EXAMPLE DSuperLUroot=$PWD
#doxygen

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name/examples/fortran
#install -d %buildroot%_docdir/%name/pdf

mv INSTALL/install.csh INSTALL/%name-install.csh
install -m755 EXAMPLE/p?drive EXAMPLE/p?drive? EXAMPLE/p?drive*_ABglobal \
	INSTALL/%name-install.csh INSTALL/test* FORTRAN/f_5x5 FORTRAN/f_pddrive \
	%buildroot%_bindir
install -p -m644 SRC/*.h %buildroot%_includedir/%name
install -m644 lib/*.a FORTRAN/*.mod %buildroot%_libdir
ln -s %_libdir/superlu_mod.mod %buildroot%_includedir/%name/
ln -s %_libdir/superlupara_mod.mod %buildroot%_includedir/%name/
cp -fR DOC/*.pdf DOC/html %buildroot%_docdir/%name/
#install -m644 DOC/latex/*.pdf %buildroot%_docdir/%name/pdf
install -p -m644 EXAMPLE/*.c EXAMPLE/*.?ua \
	%buildroot%_docdir/%name/examples
install -p -m644 FORTRAN/*.c FORTRAN/*.f90 \
	%buildroot%_docdir/%name/examples/fortran

# shared library

TOPDIR=$PWD
pushd %buildroot%_libdir
ar x libsuperlu_dist_%over.a
mpif77 -shared *.o -lparmetis -lm -lgoto2 \
	-Wl,-R%mpidir/lib \
	-Wl,-soname,libsuperlu_dist_%over.so.%somver -o \
	libsuperlu_dist_%over.so.%sover
ln -s libsuperlu_dist_%over.so.%sover \
	libsuperlu_dist_%over.so.%somver
ln -s libsuperlu_dist_%over.so.%somver \
	libsuperlu_dist_%over.so
rm -f *.o
popd

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

#files
#_bindir/%name-install.csh
#_bindir/test*

%files -n lib%name
%doc README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/*.mod
%_includedir/%name

%files -n lib%name-devel-doc
%_docdir/%name

%files examples
%doc EXAMPLE/README
%_bindir/*
#exclude %_bindir/%name-install.csh
#exclude %_bindir/test*

%changelog
* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3
- Rebuilt with OpenMPI 1.6

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Applied repocop patch: superlu_dist-3.0-alt1.diff

* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Wed May 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Disabled devel-static package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt7
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt6
- Built with GotoBLAS2 instead of ATLAS

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt5
- Fixed build
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt4
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt3
- Fixed overlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2
- Rebuilt with reformed ParMetis

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1
- Version 2.4

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt9
- Rebuilt without udapl support

* Sun Nov 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt8
- Fixed header for SuperMatrix
- Rebuilt with texlive instead of tetex

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt7
- Added shared library and additional documentation

* Sun Jun 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt6
- Fixed linking with atlas/lapack

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt5
- Rebuild with PIC

* Mon Jun 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt4
- Add links to *.mod into %_includedir/%name

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt3
- Resolve conflict with superlu

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt2
- Added explicit contflict with superlu

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Initial build for Sisyphus
