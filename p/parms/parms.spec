%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 3
%define sover %somver.2.0
Name: parms
Version: 3.2
Release: alt7
Summary: parallel Algebraic Recursive Multilevel Solvers 
License: MIT
Group: Sciences/Mathematics
Url: http://www-users.cs.umn.edu/~saad/software/pARMS/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: pARMS_%version.tar.gz

BuildPreReq: liblapack-devel libmetis-devel
BuildPreReq: %mpiimpl-devel

%description
pARMS is a library of parallel solvers for distributed sparse linear systems of
equations. It is based on a preconditioned Krylov subspace approach, using a
domain decomposition viewpoint. The plural in "Solvers" is due to the fact that
pARMS offers a large selection of preconditioners for distributed sparse linear
systems and a few of the best known accelerators.

The basic methodology used relies on a Recursive Multi-level ILU factorization
wich allows to develop many of the standard domain-decomposition type iterative
solvers in a single framework. For example, the standard Schwarz procedures are
included as are a number of Schur complement techniques.

pARMS resulted from a team effort that spanned several years. It really began in
around 1993/1994 with the development of its FORTRAN predecessor called
PSPARSLIB [developer: Y. Saad]. In 1999-2000 Brian Suchomel developed the
sequential version of ARMS. Zhongze Li developed the first version of the
parallel ARMS in around 2000-2001. The current version of pARMS is the result of
a substantial revision of this earlier code done in part by YS and to a bigger
extent by Masha Sosonkina. Many people made other contributions to pARMS.

%package -n lib%name
Summary: Shared library of pARMS
Group: System/Libraries

%description -n lib%name
pARMS is a library of parallel solvers for distributed sparse linear systems of
equations. It is based on a preconditioned Krylov subspace approach, using a
domain decomposition viewpoint. The plural in "Solvers" is due to the fact that
pARMS offers a large selection of preconditioners for distributed sparse linear
systems and a few of the best known accelerators.

The basic methodology used relies on a Recursive Multi-level ILU factorization
wich allows to develop many of the standard domain-decomposition type iterative
solvers in a single framework. For example, the standard Schwarz procedures are
included as are a number of Schur complement techniques.

This package contains shared library of pARMS.

%package -n lib%name-devel
Summary: Development files of pARMS
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
pARMS is a library of parallel solvers for distributed sparse linear systems of
equations. It is based on a preconditioned Krylov subspace approach, using a
domain decomposition viewpoint. The plural in "Solvers" is due to the fact that
pARMS offers a large selection of preconditioners for distributed sparse linear
systems and a few of the best known accelerators.

The basic methodology used relies on a Recursive Multi-level ILU factorization
wich allows to develop many of the standard domain-decomposition type iterative
solvers in a single framework. For example, the standard Schwarz procedures are
included as are a number of Schur complement techniques.

This package contains development files of pARMS.

%package -n lib%name-devel-doc
Summary: Documentation for pARMS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
pARMS is a library of parallel solvers for distributed sparse linear systems of
equations. It is based on a preconditioned Krylov subspace approach, using a
domain decomposition viewpoint. The plural in "Solvers" is due to the fact that
pARMS offers a large selection of preconditioners for distributed sparse linear
systems and a few of the best known accelerators.

The basic methodology used relies on a Recursive Multi-level ILU factorization
wich allows to develop many of the standard domain-decomposition type iterative
solvers in a single framework. For example, the standard Schwarz procedures are
included as are a number of Schur complement techniques.

This package contains development documentation for pARMS.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

%make_build TOPDIR=$PWD
%make_build TOPDIR=$PWD examples

%make_build -C examples/general
%make_build -C examples/grid

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_datadir/%name/examples
install -d %buildroot%_docdir/lib%name-devel/examples/general
install -d %buildroot%_docdir/lib%name-devel/examples/grid

install -m644 lib/* %buildroot%_libdir

install -p -m644 include/*.h src/include/*.h %buildroot%_includedir
install -p -m644 docs/* %buildroot%_docdir/lib%name-devel

pushd examples
install -m755 general/*.ex grid/*.ex %buildroot%_bindir
rm -f general/*.ex grid/*.ex general/*.o grid/*.o general/makefile grid/makefile
# petsc examples will be build after building PETSc
rm -fR petsc general/extras grid/extras
mv general/*.c general/*.F general/*.f general/*.h \
	%buildroot%_docdir/lib%name-devel/examples/general/
mv grid/*.c grid/*.F grid/*.f grid/*.h \
	%buildroot%_docdir/lib%name-devel/examples/grid/
mv * %buildroot%_datadir/%name/examples/
popd

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
mpif77 -shared * -llapack -lgoto2 \
	-Wl,-rpath,%mpidir/lib \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc COPYRIGHT LGPL README
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt7
- Rebuilt with OpenMPI 1.6

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt6
- parms_sys.h: fixed declaration conflicting

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt5
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt4
- Built with GotoBLAS2 instead of ATLAS
- Disabled static package

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt3
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Version 3.2

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt6
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt5
- Fixed overlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt4
- Rebuilt with reformed Metis

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt3
- Added shared library

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt2
- Rebuild with PIC

* Sat Jun 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt1
- Initial build for Sisyphus

