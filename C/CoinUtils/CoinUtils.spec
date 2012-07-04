%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: CoinUtils
Version: 2.8.6
Release: alt3.svn20120129
Summary: Open-source collection of classes and functions for COIN-OR project
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/CoinUtils.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CoinUtils/trunk
Source: %name-%version.tar.gz

BuildPreReq: CoinBuildTools gcc-c++ libglpk-devel
BuildPreReq: liblapack-devel %mpiimpl-devel zlib-devel bzlib-devel
BuildPreReq: CoinSample-devel CoinNetlib-devel
BuildPreReq: graphviz doxygen

%description
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

%package -n lib%name
Summary: Shared libraries of CoinUtils
Group: System/Libraries
Requires: CoinSample-data CoinNetlib-data

%description -n lib%name
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains shared libraries of CoinUtils.

%package -n lib%name-devel
Summary: Development files of CoinUtils
Group: Development/C++
Requires: lib%name = %version-%release
Requires: CoinSample-devel CoinNetlib-devel

%description -n lib%name-devel
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains development files of CoinUtils.

%package docs
Summary: Documentation for CoinUtils
Group: Development/Documentation
BuildArch: noarch

%description docs
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains development documentation for CoinUtils.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%autoreconf
%add_optflags -I%mpidir/include
%configure \
	--with-coin-instdir=%prefix \
	--with-glpk-lib=-lglpk \
	--with-glpk-incdir=%_includedir/glpk \
	--with-blas-lib=-lgoto2 \
	--with-lapack-lib=-llapack \
	--with-dot
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

pushd %name/doxydoc
doxygen doxygen.conf
popd

rm -fR %buildroot%_datadir/coin/doc \
	%buildroot%_docdir/coin

%files -n lib%name
%doc AUTHORS LICENSE
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files docs
%doc %name/doxydoc/doxydoc/html/*

%changelog
* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt3.svn20120129
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt2.svn20120129
- Fixed build

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt1.svn20120129
- Version 2.8.6

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.svn20110903
- Version 2.8.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.1-alt1.svn20110417
- Version 2.7.1

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.1
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205
- Version 2.7.0

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829.2
- Fixed overlinking of libraries

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829.1
- Fixed requirements

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829
- Initial build for Sisyphus

