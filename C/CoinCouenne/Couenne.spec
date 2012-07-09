%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define sover 0.0.0
%define oname Couenne
Name: Coin%oname
Version: 0.4.2
Release: alt2.svn20120211
Summary: Convex Over and Under ENvelopes for Nonlinear Estimation
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Couenne.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Couenne/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel liblapack-goto-devel
BuildPreReq: libmumps-devel libCoinCgl-devel libCoinBonmin-devel
BuildPreReq: libCoinClp-devel libipopt-devel CoinMiplib3-devel
BuildPreReq: libCoinCbc-devel %mpiimpl-devel CoinSample-devel
BuildPreReq: CoinNetlib-devel chrpath

%description
Couenne (Convex Over and Under ENvelopes for Nonlinear Estimation) is a
spatial branch&bound algorithm that implements linearization, bound
reduction, and branching techniques for Mixed-integer, Nonlinear
Programming (MINLP) problems. The purpose of Couenne is to find global
optima of nonconvex MINLPs.

%package -n lib%name
Summary: Shared libraries of COIN-OR Couenne
Group: System/Libraries

%description -n lib%name
Couenne (Convex Over and Under ENvelopes for Nonlinear Estimation) is a
spatial branch&bound algorithm that implements linearization, bound
reduction, and branching techniques for Mixed-integer, Nonlinear
Programming (MINLP) problems. The purpose of Couenne is to find global
optima of nonconvex MINLPs.

This package contains shared libraries of COIN-OR Couenne.

%package -n lib%name-devel
Summary: Development files of COIN-OR Couenne
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libCoinBonmin-devel

%description -n lib%name-devel
Couenne (Convex Over and Under ENvelopes for Nonlinear Estimation) is a
spatial branch&bound algorithm that implements linearization, bound
reduction, and branching techniques for Mixed-integer, Nonlinear
Programming (MINLP) problems. The purpose of Couenne is to find global
optima of nonconvex MINLPs.

This package contains development files of COIN-OR Couenne.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Couenne
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Couenne (Convex Over and Under ENvelopes for Nonlinear Estimation) is a
spatial branch&bound algorithm that implements linearization, bound
reduction, and branching techniques for Mixed-integer, Nonlinear
Programming (MINLP) problems. The purpose of Couenne is to find global
optima of nonconvex MINLPs.

This package contains development documentation for COIN-OR Couenne.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%add_optflags -I%_includedir/coin
%configure \
	--with-bonmin-incdir=%_includedir/coin \
	--with-mumps-lib=-ldmumps \
	--with-blas-lib=-lgoto2 \
	--with-lapack-lib=-llapack
sed -i 's|\(wl=\).*|\1"-Wl,"|' libtool
%make_build TOPDIR=$PWD

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

# for circular linking; this operation need 2 steps
rm -f $(find ./ -name 'libCouenne.*')
%make_build TOPDIR=$PWD ADDLIB="-Lmain/.libs -lBonCouenne" ||
	%make_build TOPDIR=$PWD ADDLIB="-Lmain/.libs -lBonCouenne"
cp -f Couenne/src/.libs/libCouenne.so.%sover \
	%buildroot%_libdir/

for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i
done

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doc/*.pdf

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.svn20120211
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.svn20120211
- Version 0.4.2

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.svn20110903
- Version 0.4.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.svn20110421
- Version 0.3.3

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20101208.4
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20101208.3
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20101208.2
- Rebuilt for debuginfo (stage 2)

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20101208.1
- Rebuilt for debuginfo (stage 1)

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20101208
- New snapshot

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20100830.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20100830.1
- Fixed linking of libraries

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.svn20100830
- Initial build for Sisyphus

