%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Cbc
Name: Coin%oname
Version: 2.9.8
Release: alt1
Summary: COIN-OR Branch-and-Cut MIP Solver
License: EPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Cbc

# https://www.coin-or.org/download/source/%oname/%oname-%version.tgz
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildRequires: libCoinUtils-devel liblapack-devel
BuildRequires: libCoinCgl-devel libCoinClp-devel libCoinOsi-devel
BuildRequires: libCoinVol-devel libCoinDyLP-devel
BuildRequires: CoinMiplib3-devel chrpath libnuma-devel

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
%setup -n %oname-%version
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,Cgl,Clp,CoinUtils,Data,Osi,ThirdParty}

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-coin-instdir=%prefix \
	--with-blas-lib=-lopenblas \
	--with-lapack-lib=-llapack \
	--with-glpk-incdir=%_includedir \
	--with-dot \
	--disable-dependency-linking
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
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

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

%files examples
%doc %oname/examples/*.c* %oname/examples/*.hpp %oname/examples/*.mps
%doc %oname/examples/*.csv %oname/examples/Makefile
#_bindir/%oname-driver

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%changelog
* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.8-alt1
- Updated to upstream stable version 2.9.8.

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.8.9-alt1.svn20140513.1
- build fixed
- gcc set to 4.9, docs not packaged

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.9-alt1.svn20140513
- Version 2.8.9

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt1.svn20131129
- Version 2.8.7

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1.svn20130827
- Version 2.8.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.8-alt1.svn20130209
- Version 2.7.8

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.7-alt3.svn20120903
- Rebuilt with glpk 4.48

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.7-alt2.svn20120903
- Rebuilt

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.7-alt1.svn20120903
- Version 2.7.7

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.6-alt3.svn20120208
- Built with OpenBLAS instead of GotoBLAS2

* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.6-alt2.svn20120208
- Rebuilt with OpenMPI 1.6

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

