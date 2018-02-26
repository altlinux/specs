%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname Cbc
Name: Coin%oname
Version: 2.7.6
Release: alt1.svn20120208
Summary: COIN-OR Branch-and-Cut MIP Solver
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Cbc.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Cbc/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel liblapack-goto-devel
BuildPreReq: libCoinCgl-devel libCoinClp-devel libCoinOsi-devel
BuildPreReq: libCoinVol-devel libCoinDyLP-devel %mpiimpl-devel
BuildPreReq: CoinMiplib3-devel chrpath

Requires: lib%name = %version-%release

%description
CBC is an open-source MILP solver. It uses many of the COIN components
and is designed to be used with CLP or dylp. It is available as a
library and as a standalone solver.

%package -n lib%name
Summary: Shared libraries of COIN-OR Branch-and-Cut MIP Solver
Group: System/Libraries
Requires: CoinMiplib3-data

%description -n lib%name
CBC is an open-source MILP solver. It uses many of the COIN components
and is designed to be used with CLP or dylp. It is available as a
library and as a standalone solver.

This package contains shared libraries of COIN-OR Branch-and-Cut MIP
Solver.

%package -n lib%name-devel
Summary: Development files of COIN-OR Branch-and-Cut MIP Solver
Group: Development/C++
Requires: lib%name = %version-%release
Requires: CoinMiplib3-devel

%description -n lib%name-devel
CBC is an open-source MILP solver. It uses many of the COIN components
and is designed to be used with CLP or dylp. It is available as a
library and as a standalone solver.

This package contains development files of COIN-OR Branch-and-Cut MIP
Solver.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Branch-and-Cut MIP Solver
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
CBC is an open-source MILP solver. It uses many of the COIN components
and is designed to be used with CLP or dylp. It is available as a
library and as a standalone solver.

This package contains development documentation for COIN-OR
Branch-and-Cut MIP Solver.

%package examples
Summary: Examples for COIN-OR Branch-and-Cut MIP Solver
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
CBC is an open-source MILP solver. It uses many of the COIN components
and is designed to be used with CLP or dylp. It is available as a
library and as a standalone solver.

This package contains examples for COIN-OR Branch-and-Cut MIP Solver.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-coin-instdir=%prefix \
	--with-blas-lib=-lgoto2 \
	--with-lapack-lib=-llapack \
	--with-glpk-incdir=%_includedir \
	--with-dot
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR
rm -f $(find %oname -name 'libOsiCbc.*') \
	$(find %oname -name 'libCbcSolver.*')
%make_build TOPDIR=$TOPDIR ADDLIB=-lCbc

#make_build -C %oname/examples TOPDIR=$TOPDIR

pushd %oname/doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

#install -m755 %oname/examples/driver %buildroot%_bindir/%oname-driver

#for i in cbc %oname-driver; do
#	chrpath -r %mpidir/lib %buildroot%_bindir/$i
#done
for i in %buildroot%_libdir/*.so %buildroot%_bindir/cbc
do
	chrpath -r %mpidir/lib $i
done

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

%files
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_bindir/cbc

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%files examples
%doc %oname/examples/*.c* %oname/examples/*.hpp %oname/examples/*.mps
%doc %oname/examples/*.csv %oname/examples/Makefile
#_bindir/%oname-driver

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.6-alt1.svn20120208
- Version 2.7.6

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.1-alt1.svn20110903
- Version 2.7.1

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20110417
- Version 2.6.4

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.svn20101213.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.svn20101213.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.svn20101213.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.svn20101213
- Version 2.6.0

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100831.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100831.1
- Fixed linking of libraries

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100831
- Initial build for Sisyphus

