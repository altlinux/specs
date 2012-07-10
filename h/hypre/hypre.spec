%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.2.6
Name: hypre
Version: 2.8.0b
Release: alt4
Summary: Scalable algorithms for solving linear systems of equations
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.llnl.gov/casc/hypre/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Source1: babel_files

Requires: lib%name-devel = %version-%release

BuildRequires(pre): rpm-build-python rpm-build-java /proc
BuildPreReq: gcc-fortran gcc-c++ %mpiimpl-devel emacs24-nox
BuildPreReq: liblapack-devel w3c-libwww-devel
BuildPreReq: libsuperlu-devel babel
BuildPreReq: java-devel-default libchasm-devel chasm python-devel
BuildPreReq: libnumpy-devel libxml2-devel python-module-libxml2
BuildPreReq: libltdl-devel

%description
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

%package -n lib%name
Summary: Shared libraries of Hypre
Group: System/Libraries

%description -n lib%name
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains shared libraries of Hypre.

%package -n lib%name-devel
Summary: Development files of Hypre
Group: Development/Other
Requires: libbabel-devel libltdl7-devel libsuperlu-devel
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains development files of Hypre.

%package -n lib%name-devel-doc
Summary: Development documentation for Hypre
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains development documentation for Hepre.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source /etc/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export includedir=%_includedir
export JNI_INCLUDES="%_libexecdir/jvm/java/include"
export MPIDIR=%mpidir
cd src

FLAGS="%optflags %optflags_shared -I%_includedir/numpy"
%add_optflags $FLAGS
%configure \
	--without-examples \
	--with-MPI \
	--with-MPI-include=%mpidir/include \
	--with-MPI-libs="mpi_f90 mpi_f77 mpi mpi_cxx" \
	--with-MPI-lib-dirs="%mpidir/lib" \
	--with-timing \
	--without-openmp \
	--with-babel \
	--with-chasm=%prefix \
	--with-blas-libs=-lgoto2 \
	--with-blas-lib-dirs=%_libdir \
	--with-lapack \
	--with-mli \
	--with-fei \
	--with-superlu \
	CC="mpicc $FLAGS" \
	CXX="mpicxx $FLAGS" \
	F77="mpif77 $FLAGS" \
	MPI_PREFIX=%mpidir
sed -i 's|^\(HYPRE_INSTALL_DIR\).*|\1 = %buildroot%prefix|' \
	config/Makefile.config
sed -i 's|^\(HYPRE_LIB_INSTALL\).*|\1 = %buildroot%_libdir|' \
	config/Makefile.config
sed -i 's|^\(HYPRE_INC_INSTALL\).*|\1 = %buildroot%_includedir/%name|' \
	config/Makefile.config
mkdir -p hypre/lib
pushd FEI_mv/femli
%make_build all CC="mpicc $FLAGS" CXX="mpicxx $FLAGS" F77="mpif77 $FLAGS"
popd
%make_build all

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

pushd src

%makeinstall_std
install -m644 hypre/lib/* %buildroot%_libdir

install -d %buildroot%_docdir/lib%name-devel-doc
rm -f ../src/docs/Makefile
cp -fR ../src/docs/* %buildroot%_docdir/lib%name-devel-doc/
rm -f %buildroot%_libdir/libsidl*
popd

# shared libraries

pushd %buildroot%_libdir
LIBS="$(ls *.a|sed 's|\.a||'|sort)"
mkdir tmp
pushd tmp
for i in $LIBS; do
	if [ "$i" != "libbHYPREClient-F" -a "$i" != "libbHYPREClient-CX" ]
	then
		ar x ../$i.a
		mpic++ -shared * -L.. $ADDLIB \
			-lsidl -llapack -lgoto2 \
			-Wl,-rpath,%mpidir/lib \
			-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
		ln -s $i.so.%sover ../$i.so.%somver
		ln -s $i.so.%somver ../$i.so
		rm -f *
		ADDLIB="-lHYPRE"
	fi
done
popd
rmdir tmp
popd

%files
%doc CHANGELOG COPYING.LESSER COPYRIGHT

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%exclude %_includedir/%name/Cnames.h
%exclude %_includedir/%name/supermatrix.h
%exclude %_includedir/%name/slu_*.h

%files -n lib%name-devel-doc
%_docdir/lib%name-devel-doc

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt4
- Rebuilt with emacs 24.1

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt2
- Fixed build

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt1
- Version 2.8.0b

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt3
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt2
- Rebuilt with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt1
- Version 2.7.0b
- Disabled static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt6
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt5
- Rebuilt for debuginfo

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt4
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt3
- Fixed overlinking of libraries

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt2
- Rebuilt without python-module-Numeric

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt1
- Version 2.6.0b

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt9
- Rebuilt with SuperLU 4.0 and emacs23

* Sun Nov 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt8
- Removed unnecessary headers

* Tue Sep 1 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt7
- Added shared libraries

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt6
- Fixed MPI check

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt5
- Rebuild with PIC

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt4
- Rebuild with OpenMPI

* Wed Apr 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt3
- Move headers into hypre subdirectory

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt2
- Remove files owned by other packages

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt1
- Initial build for Sisyphus

