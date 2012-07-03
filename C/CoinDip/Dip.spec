%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname Dip
Name: Coin%oname
Version: 0.83.1
Release: alt1.svn20110910
Summary: COIN-OR Decomposition for Integer Programming
License: Eclipse Public License v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Dip.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Dip/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinAlps-devel libCoinBcps-devel
BuildPreReq: libCoinBlis-devel libCoinCbc-devel libCoinCgl-devel
BuildPreReq: libCoinOsi-devel libCoinClp-devel
BuildPreReq: liblapack-goto-devel %mpiimpl-devel chrpath

%description
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding
algorithms for use in solving large-scale discrete optimization
problems. The framework provides a simple API for experimenting with
various decomposition-based algorithms, such as Dantzig-Wolfe
decomposition, Lagrangian relaxation, and various cutting plane methods.
Given a compact formulation and a relaxation, the framework takes care
of all algorithmic details associated with implementing any of a wide
range of decomposition-based algorithms, such as branch and cut, branch
and price, branch and cut and price, subgradient-based Lagrangian
relaxation, branch and relax and cut, and decompose and cut. The user
can specify customizations, such as methods for generating valid
inequalities and branching, in terms of the variables of the compact
formulation, without having to worry about the details of any required
reformulations. DIP is used in combination with  CHiPPS, which provides
the underlying tree search methodology.

%package -n lib%name
Summary: Shared libraries of COIN-OR Decomposition for Integer Programming
Group: System/Libraries

%description -n lib%name
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding
algorithms for use in solving large-scale discrete optimization
problems. The framework provides a simple API for experimenting with
various decomposition-based algorithms, such as Dantzig-Wolfe
decomposition, Lagrangian relaxation, and various cutting plane methods.
Given a compact formulation and a relaxation, the framework takes care
of all algorithmic details associated with implementing any of a wide
range of decomposition-based algorithms, such as branch and cut, branch
and price, branch and cut and price, subgradient-based Lagrangian
relaxation, branch and relax and cut, and decompose and cut. The user
can specify customizations, such as methods for generating valid
inequalities and branching, in terms of the variables of the compact
formulation, without having to worry about the details of any required
reformulations. DIP is used in combination with  CHiPPS, which provides
the underlying tree search methodology.

This package contains shared libraries of COIN-OR Decomposition for
Integer Programming.

%package -n lib%name-devel
Summary: Development files of COIN-OR Decomposition for Integer Programming
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding
algorithms for use in solving large-scale discrete optimization
problems. The framework provides a simple API for experimenting with
various decomposition-based algorithms, such as Dantzig-Wolfe
decomposition, Lagrangian relaxation, and various cutting plane methods.
Given a compact formulation and a relaxation, the framework takes care
of all algorithmic details associated with implementing any of a wide
range of decomposition-based algorithms, such as branch and cut, branch
and price, branch and cut and price, subgradient-based Lagrangian
relaxation, branch and relax and cut, and decompose and cut. The user
can specify customizations, such as methods for generating valid
inequalities and branching, in terms of the variables of the compact
formulation, without having to worry about the details of any required
reformulations. DIP is used in combination with  CHiPPS, which provides
the underlying tree search methodology.

This package contains development files of COIN-OR Decomposition for
Integer Programming.

%package examples
Summary: Examples for COIN-OR Decomposition for Integer Programming
Group: Development/Documentation
BuildArch: noarch

%description examples
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding
algorithms for use in solving large-scale discrete optimization
problems. The framework provides a simple API for experimenting with
various decomposition-based algorithms, such as Dantzig-Wolfe
decomposition, Lagrangian relaxation, and various cutting plane methods.
Given a compact formulation and a relaxation, the framework takes care
of all algorithmic details associated with implementing any of a wide
range of decomposition-based algorithms, such as branch and cut, branch
and price, branch and cut and price, subgradient-based Lagrangian
relaxation, branch and relax and cut, and decompose and cut. The user
can specify customizations, such as methods for generating valid
inequalities and branching, in terms of the variables of the compact
formulation, without having to worry about the details of any required
reformulations. DIP is used in combination with  CHiPPS, which provides
the underlying tree search methodology.

This package contains examples for COIN-OR Decomposition for Integer
Programming.

%package data
Summary: Data files for COIN-OR Decomposition for Integer Programming
Group: Sciences/Mathematics
BuildArch: noarch

%description data
DIP (Decomposition for Integer Programming) is an open-source extensible
software framework for implementing decomposition-based bounding
algorithms for use in solving large-scale discrete optimization
problems. The framework provides a simple API for experimenting with
various decomposition-based algorithms, such as Dantzig-Wolfe
decomposition, Lagrangian relaxation, and various cutting plane methods.
Given a compact formulation and a relaxation, the framework takes care
of all algorithmic details associated with implementing any of a wide
range of decomposition-based algorithms, such as branch and cut, branch
and price, branch and cut and price, subgradient-based Lagrangian
relaxation, branch and relax and cut, and decompose and cut. The user
can specify customizations, such as methods for generating valid
inequalities and branching, in terms of the variables of the compact
formulation, without having to worry about the details of any required
reformulations. DIP is used in combination with  CHiPPS, which provides
the underlying tree search methodology.

This package contains data files for COIN-OR Decomposition for Integer
Programming.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-alps-incdir=%_includedir/coin \
	--with-alps-lib=-lAlps \
	--with-bcps-incdir=%_includedir/coin \
	--with-bcps-lib=-lBcps \
	--with-blis-incdir=%_includedir/coin \
	--with-blis-lib=-lBlis
%make_build TOPDIR=$PWD

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%_datadir/coin/Data/%oname
cp -fR %oname/data/* %buildroot%_datadir/coin/Data/%oname/

for i in %buildroot%_libdir/*.so; do
	chrpath -r $i ||:
done

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files data
%dir %_datadir/coin
%dir %_datadir/coin/Data
%_datadir/coin/Data/%oname

%files examples
%doc %oname/examples/*

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.83.1-alt1.svn20110910
- Version 0.83.1

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82.1-alt2.svn20110910
- Fixed RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.82.1-alt1.svn20110910.1
- Rebuild with Python-2.7

* Sun Sep 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82.1-alt1.svn20110910
- Version 0.82.1

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.3-alt1.svn20110403
- Version 0.81.3

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.0-alt1.svn20101206.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.0-alt1.svn20101206.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.0-alt1.svn20101206.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.0-alt1.svn20101206
- Version 0.81.0

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.svn20100907.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.svn20100907.1
- Fixed overlinking of libraries

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.svn20100907
- Initial build for Sisyphus

