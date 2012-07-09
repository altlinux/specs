%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Blis
Name: Coin%oname
Version: 0.93.2
Release: alt2.svn20120128
Summary: BiCePS Linear Integer Solver
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/CHiPPS.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CHiPPS/Blis/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCgl-devel
BuildPreReq: libCoinOsi-devel libCoinAlps-devel libCoinBcps-devel
BuildPreReq: liblapack-devel %mpiimpl-devel chrpath

Requires: lib%name = %version-%release

%description
BLIS (BiCePS Linear Integer Solver) is an application developed on top
of BiCePS and is part of the CHiPPS library hierarchy. BLIS is a branch
and cut solver for Mixed Integer Linear Programs.

%package -n lib%name
Summary: Shared libraries of BiCePS Linear Integer Solver
Group: System/Libraries

%description -n lib%name
BLIS (BiCePS Linear Integer Solver) is an application developed on top
of BiCePS and is part of the CHiPPS library hierarchy. BLIS is a branch
and cut solver for Mixed Integer Linear Programs.

This package contains shared libraries of BiCePS Linear Integer Solver.

%package -n lib%name-devel
Summary: Development files of BiCePS Linear Integer Solver
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
BLIS (BiCePS Linear Integer Solver) is an application developed on top
of BiCePS and is part of the CHiPPS library hierarchy. BLIS is a branch
and cut solver for Mixed Integer Linear Programs.

This package contains development files of BiCePS Linear Integer Solver.

%package -n lib%name-devel-doc
Summary: Documentation for BiCePS Linear Integer Solver
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
BLIS (BiCePS Linear Integer Solver) is an application developed on top
of BiCePS and is part of the CHiPPS library hierarchy. BLIS is a branch
and cut solver for Mixed Integer Linear Programs.

This package contains development documentation for BiCePS Linear
Integer Solver.

%package examples
Summary: Examples for BiCePS Linear Integer Solver
Group: Development/Documentation
BuildArch: noarch

%description examples
BLIS (BiCePS Linear Integer Solver) is an application developed on top
of BiCePS and is part of the CHiPPS library hierarchy. BLIS is a branch
and cut solver for Mixed Integer Linear Programs.

This package contains examples for BiCePS Linear Integer Solver.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-mpi-incdir=%mpidir/include \
	--with-mpi-lib="-L%mpidir/lib -lmpi" \
	--with-alps-incdir=%_includedir/coin \
	--with-alps-lib=-lAlps \
	--with-bcps-incdir=%_includedir/coin \
	--with-bcps-lib=-lBcps
%make_build

doxygen doxydoc/doxygen.conf

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

rm -fR %buildroot%_docdir/coin

for i in %buildroot%_libdir/*.so; do
	chrpath -r %mpidir/lib $i ||:
done

%files
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc doxydoc/html/*

%files examples
%doc %oname/examples/*

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.2-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.2-alt1.svn20120128
- Version 0.93.2

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92-alt2.svn20110903
- Fixed RPATH

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92-alt1.svn20110903
- Version 0.92

* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.7
- Fixed build

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.6
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.5
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.4
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.3
- Rebuilt with CoinBuildTools 0.6.1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204.1
- Fixed overlinking of libraries

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.2-alt1.svn20100204
- Initial build for Sisyphus

