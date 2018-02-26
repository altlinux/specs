%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname Bcps
Name: Coin%oname
Version: 0.93.2
Release: alt1.svn20120128
Summary: Make up the CHiPPS (COIN High Performance Parallel Search Framework) library hierarchy
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/CHiPPS
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CHiPPS/Bcps/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinOsi-devel
BuildPreReq: libCoinCgl-devel libCoinAlps-devel %mpiimpl-devel

%description
BiCePS is one of the libraries that make up the CHiPPS (COIN High
Performance Parallel Search Framework) library hierarchy. It implements
that data-handling functions needed to support development of many types
of relaxation-based branch-and-bound algorithms, especially for solving
mathematical programs. It is intended to capture the implementation of
methods common to all such algorithms without assuming anything about
the structure of the mathematical program or the bounding method used.

%package -n lib%name
Summary: Shared libraries of COIN-OR BiCePS
Group: System/Libraries

%description -n lib%name
BiCePS is one of the libraries that make up the CHiPPS (COIN High
Performance Parallel Search Framework) library hierarchy. It implements
that data-handling functions needed to support development of many types
of relaxation-based branch-and-bound algorithms, especially for solving
mathematical programs. It is intended to capture the implementation of
methods common to all such algorithms without assuming anything about
the structure of the mathematical program or the bounding method used.

This package contains shared libraries of COIN-OR BiCePS.

%package -n lib%name-devel
Summary: Development files of COIN-OR BiCePS
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
BiCePS is one of the libraries that make up the CHiPPS (COIN High
Performance Parallel Search Framework) library hierarchy. It implements
that data-handling functions needed to support development of many types
of relaxation-based branch-and-bound algorithms, especially for solving
mathematical programs. It is intended to capture the implementation of
methods common to all such algorithms without assuming anything about
the structure of the mathematical program or the bounding method used.

This package contains development files of COIN-OR BiCePS.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR BiCePS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
BiCePS is one of the libraries that make up the CHiPPS (COIN High
Performance Parallel Search Framework) library hierarchy. It implements
that data-handling functions needed to support development of many types
of relaxation-based branch-and-bound algorithms, especially for solving
mathematical programs. It is intended to capture the implementation of
methods common to all such algorithms without assuming anything about
the structure of the mathematical program or the bounding method used.

This package contains development documentation for COIN-OR BiCePS.

%package examples
Summary: Examples for COIN-OR BiCePS
Group: Development/Documentation
BuildArch: noarch

%description examples
BiCePS is one of the libraries that make up the CHiPPS (COIN High
Performance Parallel Search Framework) library hierarchy. It implements
that data-handling functions needed to support development of many types
of relaxation-based branch-and-bound algorithms, especially for solving
mathematical programs. It is intended to capture the implementation of
methods common to all such algorithms without assuming anything about
the structure of the mathematical program or the bounding method used.

This package contains examples for COIN-OR BiCePS.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-mpi-incdir=%mpidir/include \
	--with-mpi-lib="-L%mpidir/lib -lmpi" \
	--with-alps-lib=-lAlps \
	--with-alps-incdir=%_includedir/coin
%make_build

doxygen doxydoc/doxygen.conf

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
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
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.2-alt1.svn20120128
- Version 0.93.2

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92-alt2.svn20110903
- Fixed RPATH

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92-alt1.svn20110903
- Version 0.92

* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.6
- Fixed build

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.5
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.4
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.3
- Rebuilt with CoinBuildTools 0.6.1

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203.1
- Fixed underlinking of libraries

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100203
- Initial build for Sisyphus

