%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname Bonmin
Name: Coin%oname
Version: 1.6
Release: alt1.svn20120208
Summary: Basic Open-source Nonlinear Mixed INteger programming
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Bonmin.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Bonmin/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: liblapack-goto-devel libmetis-devel
BuildPreReq: %mpiimpl-devel libmumps-devel CoinMiplib3-devel
BuildPreReq: CoinNetlib-devel libCoinOsi-devel libCoinUtils-devel
BuildPreReq: CoinSample-devel libCoinCbc-devel libCoinCgl-devel
BuildPreReq: libCoinClp-devel libipopt-devel libCoinDyLP-devel
BuildPreReq: libCoinVol-devel libCoinSYMPHONY-devel libCoinBcp-devel
#BuildPreReq: libCoinCouenne-devel

%description
BONMIN (Basic Open-source Nonlinear Mixed INteger programming) is an
open-source code for solving general MINLP (Mixed Integer NonLinear
Programming) problems.

%package -n lib%name
Summary: Shared libraries of COIN-OR BONMIN
Group: System/Libraries

%description -n lib%name
BONMIN (Basic Open-source Nonlinear Mixed INteger programming) is an
open-source code for solving general MINLP (Mixed Integer NonLinear
Programming) problems.

This package contains shared libraries of COIN-OR BONMIN.

%package -n lib%name-devel
Summary: Development files of COIN-OR BONMIN
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
BONMIN (Basic Open-source Nonlinear Mixed INteger programming) is an
open-source code for solving general MINLP (Mixed Integer NonLinear
Programming) problems.

This package contains development files of COIN-OR BONMIN.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR BONMIN
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
BONMIN (Basic Open-source Nonlinear Mixed INteger programming) is an
open-source code for solving general MINLP (Mixed Integer NonLinear
Programming) problems.

This package contains development documentation for COIN-OR BONMIN.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
DEFS="-DCOIN_HAS_BCP=1 -DCOIN_HAS_BLAS=1 -DCOIN_HAS_LAPACK=1"
DEFS="$DEFS -DCOIN_HAS_GLPK=1 -DCOIN_HAS_COUENNE=1"
INCS="-I%mpidir/include -I%mpidir/include/metis"
INCS="$INCS -I%_includedir/glpk -I%_includedir/coin"
%add_optflags $DEFS $INCS
sed -i 's|^\(coin_has_couenne\).*|\1=../../../..|' configure
sed -i 's|^\(coin_has_couenne\).*|\1=../../../../..|' %oname/configure
%configure \
	--with-bonminbcp \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk \
	--with-metis-lib="-L%mpidir/lib -lparmetis" \
	--with-metis-incdir=%mpidir/include/metis \
	--with-mumps-lib=-ldmumps \
	--with-bcp-incdir=%_includedir/coin \
	--with-couenne-lib="-lBonCouenne -lCouenne" \
	--with-couenne-incdir=%_includedir/coin
%make_build TOPDIR=$PWD

pushd doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -p -m644 %oname/src/Interfaces/BonCurvatureEstimator.hpp \
	%oname/src/Interfaces/BonExitCodes.hpp \
	%oname/src/Interfaces/BonTMINLP2OsiLP.hpp \
	%oname/src/Algorithms/QuadCuts/BonLinearCutsGenerator.hpp \
	%buildroot%_includedir/coin

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doc/*.pdf %oname/examples doxydoc/Doc/html

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.svn20120208
- Version 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.svn20110903
- Fixed RPATH

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20110903.1
- Version 1.5.0 (with CoinCouenne)

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20110903
- Version 1.5.0 (bootstrap: without CoinCouenne)

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20110417.1
- Built with CoinCouenne

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20110417
- New snapshot (bootstrap)

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20101209.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20101209.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20101209.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20101209
- New snapshot

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20100830.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20100830.2
- Fixed linking of libraries

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20100830.1
- Built with COIN-OR Couenne

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.svn20100830
- Initial build for Sisyphus

