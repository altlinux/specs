%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Smi
Name: Coin%oname
Version: 0.92.1
Release: alt3.svn20120129
Summary: COIN-OR Stochastic Modeling Interface
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Smi.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Smi/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinCbc-devel libCoinCgl-devel
BuildPreReq: libCoinClp-devel libCoinOsi-devel %mpiimpl-devel
BuildPreReq: CoinStochastic-data libreadline-devel
BuildPreReq: libCoinFlopCpp-devel libtinfo-devel

%description
Smi is an open-source interface for modeling stochastic linear
programming problems. Currently it supports: a scenario tree structure
for multiperiod stochastic data, an implementation of a Stochastic MPS
(SMPS) reader, direct interfaces for generating scenario trees from
paths and from discrete random variables, generating the deterministic
equivalent problem for OSI compatible solvers, and parsing the solutions
by stage and scenario.

%package -n lib%name
Summary: Shared libraries of COIN-OR Stochastic Modeling Interface
Group: System/Libraries

%description -n lib%name
Smi is an open-source interface for modeling stochastic linear
programming problems. Currently it supports: a scenario tree structure
for multiperiod stochastic data, an implementation of a Stochastic MPS
(SMPS) reader, direct interfaces for generating scenario trees from
paths and from discrete random variables, generating the deterministic
equivalent problem for OSI compatible solvers, and parsing the solutions
by stage and scenario.

This package contains shared libraries of COIN-OR Stochastic Modeling
Interface.

%package -n lib%name-devel
Summary: Development files of COIN-OR Stochastic Modeling Interface
Group: Development/C++
Requires: lib%name = %version-%release
Requires: CoinStochastic-data

%description -n lib%name-devel
Smi is an open-source interface for modeling stochastic linear
programming problems. Currently it supports: a scenario tree structure
for multiperiod stochastic data, an implementation of a Stochastic MPS
(SMPS) reader, direct interfaces for generating scenario trees from
paths and from discrete random variables, generating the deterministic
equivalent problem for OSI compatible solvers, and parsing the solutions
by stage and scenario.

This package contains development files of COIN-OR Stochastic Modeling
Interface.

%package examples
Summary: Examples for COIN-OR Stochastic Modeling Interface
Group: Development/Documentation
BuildArch: noarch

%description examples
Smi is an open-source interface for modeling stochastic linear
programming problems. Currently it supports: a scenario tree structure
for multiperiod stochastic data, an implementation of a Stochastic MPS
(SMPS) reader, direct interfaces for generating scenario trees from
paths and from discrete random variables, generating the deterministic
equivalent problem for OSI compatible solvers, and parsing the solutions
by stage and scenario.

This package contains examples for COIN-OR Stochastic Modeling
Interface.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-stochastic-datadir=%_datadir/coin/Data/Stochastic
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc %oname/examples %oname/flopcpp_examples

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt3.svn20120129
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt2.svn20120129
- New snapshot

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt2.svn20110814
- Fixed RPATH

* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20110814
- New snapshot

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20110201
- New snapshot

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20101125.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20101125.1
- Rebuilt for debuginfo

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20101125
- New snapshot

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20100617.3
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20100617.2
- Fixed overlinking of libraries

* Mon Sep 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20100617.1
- Built with COIN-OR FLOPC++

* Sat Sep 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92.1-alt1.svn20100617
- Initial build for Sisyphus

