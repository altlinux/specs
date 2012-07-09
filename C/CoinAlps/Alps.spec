%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Alps
Name: Coin%oname
Version: 1.4
Release: alt2.svn20120128
Summary: Framework for implementing parallel graph search algorithms
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/CHiPPS
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CHiPPS/Alps/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinCgl-devel libCoinOsi-devel
BuildPreReq: libCoinClp-devel %mpiimpl-devel chrpath
BuildPreReq: liblapack-devel

%description
Alps is a framework for implementing parallel graph search algorithms.
Its methodology generalizes many of the notions of an LP-based
branch-and-bound algorithm, allowing the implementation of a wide range
of algorithms with a simplified interface. Alps implements the search
handling methods required for implementing large-scale, data-intensive
parallel search algorithms, such as those used for solving discrete
optimization problems. It is the base layer of the CHiPPS (COIN High
Performance Parallel Search) library hierarchy that will includes a
library for solving mixed integer linear programs (BLIS).

%package -n lib%name
Summary: Shared libraries of COIN-OR Alps
Group: System/Libraries

%description -n lib%name
Alps is a framework for implementing parallel graph search algorithms.
Its methodology generalizes many of the notions of an LP-based
branch-and-bound algorithm, allowing the implementation of a wide range
of algorithms with a simplified interface. Alps implements the search
handling methods required for implementing large-scale, data-intensive
parallel search algorithms, such as those used for solving discrete
optimization problems. It is the base layer of the CHiPPS (COIN High
Performance Parallel Search) library hierarchy that will includes a
library for solving mixed integer linear programs (BLIS).

This package contains shared libraries of COIN-OR Alps.

%package -n lib%name-devel
Summary: Development files of COIN-OR Alps
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Alps is a framework for implementing parallel graph search algorithms.
Its methodology generalizes many of the notions of an LP-based
branch-and-bound algorithm, allowing the implementation of a wide range
of algorithms with a simplified interface. Alps implements the search
handling methods required for implementing large-scale, data-intensive
parallel search algorithms, such as those used for solving discrete
optimization problems. It is the base layer of the CHiPPS (COIN High
Performance Parallel Search) library hierarchy that will includes a
library for solving mixed integer linear programs (BLIS).

This package contains development files of COIN-OR Alps.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Alps
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Alps is a framework for implementing parallel graph search algorithms.
Its methodology generalizes many of the notions of an LP-based
branch-and-bound algorithm, allowing the implementation of a wide range
of algorithms with a simplified interface. Alps implements the search
handling methods required for implementing large-scale, data-intensive
parallel search algorithms, such as those used for solving discrete
optimization problems. It is the base layer of the CHiPPS (COIN High
Performance Parallel Search) library hierarchy that will includes a
library for solving mixed integer linear programs (BLIS).

This package contains development documentation for COIN-OR Alps.

%package examples
Summary: Examples for COIN-OR Alps
Group: Development/Documentation
BuildArch: noarch

%description examples
Alps is a framework for implementing parallel graph search algorithms.
Its methodology generalizes many of the notions of an LP-based
branch-and-bound algorithm, allowing the implementation of a wide range
of algorithms with a simplified interface. Alps implements the search
handling methods required for implementing large-scale, data-intensive
parallel search algorithms, such as those used for solving discrete
optimization problems. It is the base layer of the CHiPPS (COIN High
Performance Parallel Search) library hierarchy that will includes a
library for solving mixed integer linear programs (BLIS).

This package contains examples for COIN-OR Alps.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-coin-instdir=%prefix \
	--with-mpi-incdir=%mpidir/include \
	--with-mpi-lib="-L%mpidir/lib -lmpi" \
	--with-glpk-lib=-lglpk \
	--with-glpk-incdir=%_includedir/glpk
%make_build

doxygen doxydoc/doxygen.conf

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i ||:
done

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README %oname/TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc doxydoc/html/*

%files examples
%doc %oname/examples/*

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20120128
- Version 1.4

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20110814
- Version 1.3

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.svn20110417
- Version 1.2.2

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20101205.4
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20101205.3
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20101205.2
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20101205.1
- Fixed headers

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20101205
- New snapshot

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20100914.1
- Fixed overlinking of libraries

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.svn20100914
- Initial build for Sisyphus

