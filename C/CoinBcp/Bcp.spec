%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Bcp
Name: Coin%oname
Version: 1.3.4
Release: alt2.svn20120210
Summary: COIN-OR Branch-Cut-Price Framework
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Bcp.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Bcp/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinCgl-devel libCoinOsi-devel
BuildPreReq: libCoinClp-devel libCoinVol-devel %mpiimpl-devel

%description
BCP is a parallel framework for implementing branch, cut, and price
algorithms for solving mixed integer programs (MIPs). BCP provides the
user with an object-oriented framework that can be used to develop an
efficient problem class specific MIP solver without all the
implementational effort. involved with implementing a branch and bound
framework from scratch.

%package -n lib%name
Summary: Shared libraries of COIN-OR Branch-Cut-Price Framework
Group: System/Libraries

%description -n lib%name
BCP is a parallel framework for implementing branch, cut, and price
algorithms for solving mixed integer programs (MIPs). BCP provides the
user with an object-oriented framework that can be used to develop an
efficient problem class specific MIP solver without all the
implementational effort. involved with implementing a branch and bound
framework from scratch.

This package contains shared libraries of COIN-OR Branch-Cut-Price
Framework.

%package -n lib%name-devel
Summary: Development files of COIN-OR Branch-Cut-Price Framework
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
BCP is a parallel framework for implementing branch, cut, and price
algorithms for solving mixed integer programs (MIPs). BCP provides the
user with an object-oriented framework that can be used to develop an
efficient problem class specific MIP solver without all the
implementational effort. involved with implementing a branch and bound
framework from scratch.

This package contains development file of COIN-OR Branch-Cut-Price
Framework.

%package docs
Summary: Documentation for COIN-OR Branch-Cut-Price Framework
Group: Development/Documentation
BuildArch: noarch

%description docs
BCP is a parallel framework for implementing branch, cut, and price
algorithms for solving mixed integer programs (MIPs). BCP provides the
user with an object-oriented framework that can be used to develop an
efficient problem class specific MIP solver without all the
implementational effort. involved with implementing a branch and bound
framework from scratch.

This package contains development documentation and examples for COIN-OR
Branch-Cut-Price Framework.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-mpi-incdir=%mpidir/include \
	--with-mpi-lib="-L%mpidir/lib -Wl,-rpath,%mpidir/lib -lmpi"
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README %oname/TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files docs
%doc %oname/doc/*.pdf
%doc %oname/examples

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2.svn20120210
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.svn20120210
- Version 1.3.4

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.svn20110717
- Fixed RPATH

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20110717
- Version 1.3.0

* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.6
- Fixed build

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.5
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.4
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.3
- Rebuilt with CoinBuildTools 0.6.1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226.1
- Fixed overlinking of libraries

* Mon Sep 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20091226
- Initial build for Sisyphus

