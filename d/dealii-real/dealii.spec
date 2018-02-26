%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname dealii
%define scalar_type real
%define ldir %_libexecdir/petsc-%scalar_type

Name: %oname-%scalar_type
Version: 7.2
Release: alt4.pre.svn20120224
Summary: A Finite Element Differential Equations Analysis Library (%scalar_type scalars)
License: QPL v1.0
Group: Sciences/Mathematics
Url: http://www.dealii.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.dealii.org/svn/dealii/trunk
Source: %name-%version.tar

BuildPreReq: python-module-petsc-config zlib-devel
BuildPreReq: gcc-c++ doxygen graphviz %mpiimpl-devel libqt4-devel
BuildPreReq: libpetsc-%scalar_type-devel libslepc-%scalar_type-devel
BuildPreReq: libarprec-devel libnetcdf-mpi-devel libgsl-devel
BuildPreReq: libtbb-devel libopendx-devel libp4est-devel
BuildPreReq: libstratimikos10-devel libbelos10-devel librtop10-devel
BuildPreReq: libsacado10-devel libthyra10-devel libtrilinos10-devel
BuildPreReq: libmumps-devel libhypre-devel libsuitesparse-devel
BuildPreReq: chrpath rpm-macros-make boost-signals-devel

Requires: lib%name = %version-%release

%description
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

The main aim of deal.II is to enable rapid development of modern finite
element codes, using among other aspects adaptive meshes and a wide
array of tools classes often used in finite element program. Writing
such programs is a non-trivial task, and successful programs tend to
become very large and complex. We believe that this is best done using a
program library that takes care of the details of grid handling and
refinement, handling of degrees of freedom, input of meshes and output
of results in graphics formats, and the like. Likewise, support for
several space dimensions at once is included in a way such that programs
can be written independent of the space dimension without unreasonable
penalties on run-time and memory consumption.

%package devel-common
Summary: Development common files for deal.II (%scalar_type scalars)
Group: Development/C++
Conflicts: lib%name < %version-%release

%description devel-common
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development common files for deal.II.

%package data
Summary: Data files for deal.II (%scalar_type scalars)
Group: Sciences/Mathematics
BuildArch: noarch
Conflicts: lib%name < %version-%release

%description data
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains data files for deal.II.

%package -n lib%name
Summary: Shared libraries of deal.II (%scalar_type scalars)
Group: System/Libraries
Requires: %name-data = %version-%release

%description -n lib%name
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains shared libraries of deal.II.

%package -n lib%name-devel
Summary: Development files of deal.II (%scalar_type scalars)
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: %name-devel-common = %version-%release
Requires: libpetsc-%scalar_type-devel
Requires: libslepc-%scalar_type-devel
Requires: libtrilinos10-devel
Requires: libtbb-devel

%description -n lib%name-devel
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development files of deal.II.

%package -n lib%name-debug
Summary: Shared debug libraries of deal.II (%scalar_type scalars)
Group: System/Libraries
Requires: %name-data = %version-%release

%description -n lib%name-debug
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains shared debug libraries of deal.II.

%package -n lib%name-debug-devel
Summary: Debug development files of deal.II (%scalar_type scalars)
Group: Development/C++
BuildArch: noarch
Requires: lib%name-debug = %version-%release
Requires: %name-devel-common = %version-%release
Requires: libpetsc-%scalar_type-devel
Requires: libslepc-%scalar_type-devel
Requires: libtrilinos10-devel
Requires: libtbb-debug-devel

%description -n lib%name-debug-devel
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains debug development files of deal.II.

%package -n lib%oname-devel-doc
Summary: Documentation and examples for deal.II
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc
deal.II is a C++ program library targeted at the computational solution
of partial differential equations using adaptive finite elements. It
uses state-of-the-art programming techniques to offer you a modern
interface to the complex data structures and algorithms required.

This package contains development documentation and examples for
deal.II.

%prep
%setup

rm -fR contrib/tbb contrib/boost contrib/umfpack contrib/dx
sed -i 's|@PETSC_DIR@|%ldir|g' configure.in

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
export PATH=$PATH:%_qt4dir/bin
export MPIDIR=%mpidir

%autoreconf
INCS="-I%_includedir/hypre -I%_includedir/gsl -I%_includedir/tbb"
DEFS="-DBOOST_FILESYSTEM_VERSION=2 -DHAS_C99_TR1_CMATH"
%add_optflags $INCS $DEFS -fno-strict-aliasing -std=gnu99
%configure \
	--enable-mpi \
	--enable-threads \
	--enable-shared \
	--with-multithreading \
	--with-boost=%prefix \
	--with-petsc=$PETSC_DIR \
	--with-slepc=$PETSC_DIR \
	--with-trilinos=%prefix \
	--with-trilinos-libs=%_libdir \
	--with-arpack=%prefix \
	--with-mumps=%prefix \
	--with-scalapack=%prefix \
	--with-blacs=%prefix \
	--with-blas=goto2 \
	--with-zlib=z \
	--with-netcdf=%mpidir \
	--with-netcdf-include=%mpidir/include/netcdf-3 \
	--with-metis=%mpidir \
	--with-metis-libs=%_libdir \
	--with-umfpack-include=%_includedir/suitesparse \
	--with-lapack=lapack \
	--with-p4est=%prefix
mkdir -p lib/optimized
#mkdir -p lib/debug
%make_build_ext contrib TOPDIR=$PWD
%make_ext optimized TOPDIR=$PWD

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

install -d %buildroot$PETSC_DIR/bin
install -d %buildroot$PETSC_DIR/lib
install -d %buildroot$PETSC_DIR/include
install -d %buildroot$PETSC_DIR/meshes

install -m755 lib/bin/* %buildroot$PETSC_DIR/bin
mv lib/*.so* %buildroot$PETSC_DIR/lib/
cp -fR include/* %buildroot$PETSC_DIR/include/
install -m644 lib/meshes/* %buildroot$PETSC_DIR/meshes

install -d %buildroot/$PETSC_DIR/share/dealII
cp -fR common %buildroot/$PETSC_DIR/share/dealII/

for i in %buildroot$PETSC_DIR/lib/*.so; do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib $i
done
for i in report_features make_dependencies expand_instantiations
do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib \
		%buildroot$PETSC_DIR/share/dealII/common/scripts/$i
done

chmod +r %buildroot$PETSC_DIR/lib/*.so*

%files
%doc doc/license.html
%ldir/bin/*

%files devel-common
%ldir/include/*
%ldir/share/dealII

%files data
%ldir/meshes

%files -n lib%name
%ldir/lib/*.so.*
%exclude %ldir/lib/*.g.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%exclude %ldir/lib/*.g.so

%if "%scalar_type" == "real"
%files -n lib%oname-devel-doc
%doc doc examples
%endif

%changelog
* Sat Jun 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt4.pre.svn20120224
- Rebuilt with OpenMPI 1.6

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt3.pre.svn20120224
- Rebuilt with Boost 1.49.0

* Sat Feb 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt2.pre.svn20120224
- New snapshot

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt2.pre.svn20111204
- Rebuilt with Trilinos 10.10.0

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.pre.svn20111204
- Version 7.2.pre

* Thu Nov 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826.2
- Rebuilt with Trilinos 10.8.1

* Wed Aug 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826.1
- Release up

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110826
- New snapshot

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110504.1
- Rebuilt with Boost 1.47.0

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110504
- New snapshot

* Mon Apr 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.3
- Rebuilt with libnetcdf7

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.2
- Fixed permissions for libraries

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331.1
- Built with GotoBLAS2 instead of ATLAS

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110331
- New snapshot
- Disabled debug libraries (we have debuginfo packages now)

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121.2
- Rebuilt with Boost 1.46.1

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121.1
- Fixed build by using internal Boost instead of system
- Rebuilt with debuginfo

* Thu Jan 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1-alt1.pre.svn20110121
- Version 7.1.pre
- Added debug subpackages

* Sat Jan 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1.pre.svn20101223
- Initial build for Sisyphus

