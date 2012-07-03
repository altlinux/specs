%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname Vol
Name: Coin%oname
Version: 1.3.3
Release: alt1.svn20120128
Summary: COIN-OR Volume Algorithm
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Vol.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Vol/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen libglpk-devel CoinBuildTools gcc-c++ %mpiimpl-devel
BuildPreReq: libCoinOsi-devel graphviz

%description
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal
solution comes from estimating the volumes below the faces of the dual
problem. This is an approximate method so the primal vector might have
small infeasiblities that are negligible in many practical settings. The
original subgradient algorithm produces only dual solutions.

%package -n lib%name
Summary: Shared libraries of COIN-OR Volume Algorithm
Group: System/Libraries

%description -n lib%name
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal
solution comes from estimating the volumes below the faces of the dual
problem. This is an approximate method so the primal vector might have
small infeasiblities that are negligible in many practical settings. The
original subgradient algorithm produces only dual solutions.

This package contains shared libraries of COIN-OR Volume Algorithm.

%package -n lib%name-devel
Summary: Development files of COIN-OR Volume Algorithm
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal
solution comes from estimating the volumes below the faces of the dual
problem. This is an approximate method so the primal vector might have
small infeasiblities that are negligible in many practical settings. The
original subgradient algorithm produces only dual solutions.

This package contains development files of COIN-OR Volume Algorithm.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Volume Algorithm
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal
solution comes from estimating the volumes below the faces of the dual
problem. This is an approximate method so the primal vector might have
small infeasiblities that are negligible in many practical settings. The
original subgradient algorithm produces only dual solutions.

This package contains development documentation for COIN-OR Volume
Algorithm.

%package examples
Summary: Examples for COIN-OR Volume Algorithm
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
Vol (Volume Algorithm) is an open-source implementation of a subgradient
method that produces primal as well as dual solutions. The primal
solution comes from estimating the volumes below the faces of the dual
problem. This is an approximate method so the primal vector might have
small infeasiblities that are negligible in many practical settings. The
original subgradient algorithm produces only dual solutions.

This package contains examples for COIN-OR Volume Algorithm.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure
%make_build TOPDIR=$PWD MPIDIR=%mpidir
rm -f %oname/src/OsiVol/.libs/libOsiVol.* \
	%oname/src/OsiVol/libOsiVol.la
%make_build TOPDIR=$PWD MPIDIR=%mpidir ADDLIB=-lVol

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

pushd %oname/examples
rm -f VolLp/*.o VolLp/vollp \
	VolUfl/*.o VolUfl/ufl \
	Volume-LP/*.o Volume-LP/volume-lp
popd

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doc/*.pdf

%files examples
#_bindir/*
%doc %oname/examples/*

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.svn20120128
- Version 1.3.3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.svn20110814
- Fixed RPATH

* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20110814
- Version 1.3.1

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.svn20110403
- Version 1.2.2

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20101208.2
- Added -g for compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20101208.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20101208
- Version 1.2.0

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.svn20100819.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.svn20100819.1
- Fixed linking of libraries

* Wed Sep 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.svn20100819
- Initial build for Sisyphus

