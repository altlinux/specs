%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Osi
Name: Coin%oname
Version: 0.107.8
Release: alt1
Summary: Coin Open Solver Interface
License: EPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Osi

# https://www.coin-or.org/download/source/%oname/%oname-%version.tgz
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: libglpk-devel CoinBuildTools gcc-c++
BuildRequires: libCoinUtils-devel liblapack-devel chrpath libnuma-devel
BuildRequires: doxygen graphviz CoinSample-devel CoinNetlib-devel

%description
The COIN-OR Open Solver Interface is a uniform API for interacting with
callable solver libraries. It supports linear programming solvers as
well as the ability to "finish off" a mixed-integer problem calling the
solver library's MIP solver. Currently, the following solvers are
supported: COIN-OR LP solver (OsiClp) and COIN-OR Branch and Cut solver
(CoinBcp); CPLEX (OsiCpx); DyLP (OsiDylp); FortMP (OsiFmp); GLPK, the
GNU Linear Programming Kit (OsiGlpk); Mosek (OsiMsk); OSL, the IBM
Optimization Subroutine Library (OsiOsl); SYMPHONY (OsiSym); The Volume
Algorithm (OsiVol); XPRESS-MP (OsiXpr).

%package -n lib%name
Summary: Shared libraries of COIN-OR Open Solver Interface
Group: System/Libraries

%description -n lib%name
The COIN-OR Open Solver Interface is a uniform API for interacting with
callable solver libraries. It supports linear programming solvers as
well as the ability to "finish off" a mixed-integer problem calling the
solver library's MIP solver. Currently, the following solvers are
supported: COIN-OR LP solver (OsiClp) and COIN-OR Branch and Cut solver
(CoinBcp); CPLEX (OsiCpx); DyLP (OsiDylp); FortMP (OsiFmp); GLPK, the
GNU Linear Programming Kit (OsiGlpk); Mosek (OsiMsk); OSL, the IBM
Optimization Subroutine Library (OsiOsl); SYMPHONY (OsiSym); The Volume
Algorithm (OsiVol); XPRESS-MP (OsiXpr).

This package contains shared libraries of COIN-OR Open Solver Interface.

%package -n lib%name-devel
Summary: Development files of COIN-OR Open Solver Interface
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The COIN-OR Open Solver Interface is a uniform API for interacting with
callable solver libraries. It supports linear programming solvers as
well as the ability to "finish off" a mixed-integer problem calling the
solver library's MIP solver. Currently, the following solvers are
supported: COIN-OR LP solver (OsiClp) and COIN-OR Branch and Cut solver
(CoinBcp); CPLEX (OsiCpx); DyLP (OsiDylp); FortMP (OsiFmp); GLPK, the
GNU Linear Programming Kit (OsiGlpk); Mosek (OsiMsk); OSL, the IBM
Optimization Subroutine Library (OsiOsl); SYMPHONY (OsiSym); The Volume
Algorithm (OsiVol); XPRESS-MP (OsiXpr).

This package contains development files of COIN-OR Open Solver
Interface.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Open Solver Interface
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The COIN-OR Open Solver Interface is a uniform API for interacting with
callable solver libraries. It supports linear programming solvers as
well as the ability to "finish off" a mixed-integer problem calling the
solver library's MIP solver. Currently, the following solvers are
supported: COIN-OR LP solver (OsiClp) and COIN-OR Branch and Cut solver
(CoinBcp); CPLEX (OsiCpx); DyLP (OsiDylp); FortMP (OsiFmp); GLPK, the
GNU Linear Programming Kit (OsiGlpk); Mosek (OsiMsk); OSL, the IBM
Optimization Subroutine Library (OsiOsl); SYMPHONY (OsiSym); The Volume
Algorithm (OsiVol); XPRESS-MP (OsiXpr).

This package contains development documentation for COIN-OR Open Solver
Interface.

%package examples
Summary: Examples for COIN-OR Open Solver Interface
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
The COIN-OR Open Solver Interface is a uniform API for interacting with
callable solver libraries. It supports linear programming solvers as
well as the ability to "finish off" a mixed-integer problem calling the
solver library's MIP solver. Currently, the following solvers are
supported: COIN-OR LP solver (OsiClp) and COIN-OR Branch and Cut solver
(CoinBcp); CPLEX (OsiCpx); DyLP (OsiDylp); FortMP (OsiFmp); GLPK, the
GNU Linear Programming Kit (OsiGlpk); Mosek (OsiMsk); OSL, the IBM
Optimization Subroutine Library (OsiOsl); SYMPHONY (OsiSym); The Volume
Algorithm (OsiVol); XPRESS-MP (OsiXpr).

This package contains examples for COIN-OR Open Solver Interface.

%prep
%setup -n %oname-%version
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,CoinUtils,Data,ThirdParty}

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%add_optflags -I%mpidir/include
%configure \
	--with-coin-instdir=%prefix \
	--with-glpk-lib=-lglpk \
	--with-glpk-incdir=%_includedir/glpk \
	--with-blas-lib=-lgoto2 \
	--with-lapack-lib=-llapack \
	--with-dot \
	--disable-cplex-libcheck \
	--disable-mosek-libcheck \
	--disable-xpress-libcheck \
	--disable-gurobi-libcheck \
	--disable-soplex-libcheck \
	--disable-dependency-linking
sed -i 's|\-lglpk||g' Osi/examples/Makefile
export PKG_CONFIG_PATH=$PWD/Osi
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR
# broken now
#make_build -C %oname/examples TOPDIR=$TOPDIR MPIDIR=%mpidir

pushd %oname/doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

install -d %buildroot%_bindir
#install %oname/examples/basic %buildroot%_bindir/%oname-basic

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i
done

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%files examples
%doc %oname/examples/*.?pp %oname/examples/Makefile %oname/examples/README
#_bindir/*

%changelog
* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.107.8-alt1
- Updated to stable upstream version 0.107.8.

* Tue Feb 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.106.4-alt1.svn20140217.1
- build fixed

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.106.4-alt1.svn20140217
- New snapshot

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.106.4-alt1.svn20131122
- Version 0.106.4

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.106.1-alt1.svn20130830
- Version 0.106.1

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.7-alt1.svn20130205
- Version 0.105.7

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.5-alt3.svn20120901
- Fixed headers for work with glpk 4.48

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.5-alt2.svn20120901
- Rebuilt with glpk 4.48

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.5-alt1.svn20120901
- Version 0.105.5

* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.3-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.3-alt1.svn20120128
- Version 0.105.3

* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.105.1-alt1.svn20110922
- Version 0.105.1

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.2-alt1.svn20110417
- Version 0.104.2

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.1-alt1.svn20101209.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.1-alt1.svn20101209.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.1-alt1.svn20101209.1
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.1-alt1.svn20101209
- Version 0.104.1

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.103.0-alt1.svn20100829.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.103.0-alt1.svn20100829.1
- Fixed linking of libraries and examples

* Wed Sep 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.103.0-alt1.svn20100829
- Initial build for Sisyphus

