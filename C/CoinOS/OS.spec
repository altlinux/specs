%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname OS
Name: Coin%oname
Version: 2.4.2
Release: alt2.svn20120210
Summary: COIN-OR Optimization Services (OS)
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/OS.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/OS/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCbc-devel
BuildPreReq: libCoinCgl-devel libCoinCppAD-devel libCoinDyLP-devel
BuildPreReq: libipopt-devel libCoinOsi-devel libCoinSYMPHONY-devel
BuildPreReq: libCoinVol-devel libCoinBcp-devel libCoinBonmin-devel
BuildPreReq: libCoinCouenne-devel CoinSample-devel
BuildPreReq: liblapack-devel libmumps-devel
BuildPreReq: %mpiimpl-devel boost-devel chrpath

Requires: lib%name = %version-%release

%description
The objective of Optimization Services (OS) is to provide a set of
standards for representing optimization instances, results, solver
options, and communication between clients and solvers in a distributed
environment using Web Services.

%package -n lib%name
Summary: Shared libraries of COIN-OR Optimization Services (OS)
Group: System/Libraries

%description -n lib%name
The objective of Optimization Services (OS) is to provide a set of
standards for representing optimization instances, results, solver
options, and communication between clients and solvers in a distributed
environment using Web Services.

This package contains shared libraries of COIN-OR Optimization Services
(OS).

%package -n lib%name-devel
Summary: Development files of COIN-OR Optimization Services (OS)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The objective of Optimization Services (OS) is to provide a set of
standards for representing optimization instances, results, solver
options, and communication between clients and solvers in a distributed
environment using Web Services.

This package contains development files of COIN-OR Optimization Services
(OS).

%package docs
Summary: Documentation for COIN-OR Optimization Services (OS)
Group: Documentation
BuildArch: noarch

%description docs
The objective of Optimization Services (OS) is to provide a set of
standards for representing optimization instances, results, solver
options, and communication between clients and solvers in a distributed
environment using Web Services.

This package contains documentation for COIN-OR Optimization Services
(OS).

%package examples
Summary: Examples for COIN-OR Optimization Services (OS)
Group: Sciences/Mathematics
BuildArch: noarch

%description examples
The objective of Optimization Services (OS) is to provide a set of
standards for representing optimization instances, results, solver
options, and communication between clients and solvers in a distributed
environment using Web Services.

This package contains examples for COIN-OR Optimization Services
(OS).

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
DEFS="-DCOIN_HAS_BONMIN=1 -DCOIN_HAS_COUENNE=1 -DCOIN_HAS_CPPAD=1"
DEFS="$DEFS -DCOIN_HAS_BCP=1"
%add_optflags $DEFS -I%_includedir/coin -I%mpidir/include
%configure \
	--enable-debug \
	--disable-openmp \
	--with-boncouenne \
	--with-cppad-incdir=%_includedir/cppad \
	--with-cppad-lib=-lcppad_ipopt \
	--with-bonmin-incdir=%_includedir/coin \
	--with-couenne-incdir=%_includedir/coin \
	--with-bcp-incdir=%_includedir/coin \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk \
	--with-mumps-lib=-ldmumps
sed -i 's|\(wl=\).*|\1"-Wl,"|' libtool
%make_build OSSRCDIR=$PWD/%oname

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std OSSRCDIR=$PWD/%oname

rm -fR %buildroot%_datadir/coin/doc

for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i ||:
done

%files
%doc %oname/AUTHORS %oname/ChangeLog %oname/LICENSE %oname/README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files docs
%doc %oname/doc/*.pdf

%files examples
#doc %oname/data %oname/examples %oname/CoinAllExamples
%doc %oname/data %oname/misc %oname/v2.0 %oname/test
%doc %oname/stylesheets %oname/schemas %oname/wsdl
%doc %oname/applications

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt2.svn20120210
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20120210
- Version 2.4.2

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt2.svn20110930
- Fixed RPATH

* Tue Oct 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.svn20110930
- Version 2.4.0

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5-alt1.svn20110420
- Version 2.3.5

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20101218.3
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20101218.2
- Rebuilt with Boost 1.46.1

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20101218.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20101218
- Version 2.3.0

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20100903.2
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20100903.1
- Fixed linking of libraries

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.svn20100903
- Initial build for Sisyphus

