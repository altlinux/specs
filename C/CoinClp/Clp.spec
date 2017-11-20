%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Clp
Name: Coin%oname
Version: 1.16.10
Release: alt1
Summary: COIN-OR Linear Programming Solver
License: EPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Clp

# https://www.coin-or.org/download/source/%oname/%oname-%version.tgz
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: doxygen graphviz CoinBuildTools gcc-c++
BuildRequires: libCoinOsi-devel libCoinVol-devel chrpath libmumps-devel
BuildRequires: libreadline-devel libtinfo-devel libglpk-devel
BuildRequires: libsuitesparse-devel libnuma-devel

Requires: lib%name = %version-%release

%description
CLP is a high quality open-source LP solver. Its main strengths are its
Dual and Primal Simplex algorithms. It also has a barrier algorithm for
Linear and Quadratic objectives. There are limited facilities for
Nonlinear and Quadratic objectives using the Simplex algorithm. It is
available as a library and as a standalone solver. It was written by
John Forrest, jjforre at us.ibm.com.

%package -n lib%name
Summary: Shared libraries of COIN-OR Linear Programming Solver
Group: System/Libraries

%description -n lib%name
CLP is a high quality open-source LP solver. Its main strengths are its
Dual and Primal Simplex algorithms. It also has a barrier algorithm for
Linear and Quadratic objectives. There are limited facilities for
Nonlinear and Quadratic objectives using the Simplex algorithm. It is
available as a library and as a standalone solver. It was written by
John Forrest, jjforre at us.ibm.com.

This package contains shared libraries of COIN-OR Linear Programming
Solver.

%package -n lib%name-devel
Summary: Development files of COIN-OR Linear Programming Solver
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
CLP is a high quality open-source LP solver. Its main strengths are its
Dual and Primal Simplex algorithms. It also has a barrier algorithm for
Linear and Quadratic objectives. There are limited facilities for
Nonlinear and Quadratic objectives using the Simplex algorithm. It is
available as a library and as a standalone solver. It was written by
John Forrest, jjforre at us.ibm.com.

This package contains development files of COIN-OR Linear Programming
Solver.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Linear Programming Solver
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
CLP is a high quality open-source LP solver. Its main strengths are its
Dual and Primal Simplex algorithms. It also has a barrier algorithm for
Linear and Quadratic objectives. There are limited facilities for
Nonlinear and Quadratic objectives using the Simplex algorithm. It is
available as a library and as a standalone solver. It was written by
John Forrest, jjforre at us.ibm.com.

This package contains development documentation for COIN-OR Linear
Programming Solver.

%package examples
Summary: Examples for COIN-OR Linear Programming Solver
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
CLP is a high quality open-source LP solver. Its main strengths are its
Dual and Primal Simplex algorithms. It also has a barrier algorithm for
Linear and Quadratic objectives. There are limited facilities for
Nonlinear and Quadratic objectives using the Simplex algorithm. It is
available as a library and as a standalone solver. It was written by
John Forrest, jjforre at us.ibm.com.

This package contains examples for COIN-OR Linear Programming
Solver.

%prep
%setup -n %oname-%version
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,CoinUtils,Data,Osi,ThirdParty}

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -I%mpidir/include -I%_includedir/suitesparse -DOMPI_SKIP_MPICXX
%autoreconf
sed -i 's|\(termcap\)|\1 tinfo|' Clp/configure
%configure \
	--with-coin-instdir=%prefix \
	--with-blas-lib=-lblas \
	--with-lapack-lib=-llapack \
	--with-osi-lib=-lOsi \
	--with-osi-incdir=%_includedir/coin \
	--with-glpk-lib=-lglpk \
	--with-mumps-lib="-ldmumps -lzmumps -lsmumps -lcmumps -lmumps_common -lpord" \
	--with-dot \
	--disable-dependency-linking
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR
rm -f $(find ./ -name 'libOsiClp.*') $(find ./ -name 'libClpSolver.*')
%make_build TOPDIR=$TOPDIR ADDLIB=-lClp

#make_build -C %oname/examples TOPDIR=$TOPDIR MPIDIR=%mpidir

pushd %oname/doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

install -d %buildroot%_bindir
#install -m755 %oname/examples/driver %buildroot%_bindir/%oname-driver

install -p -m644 Clp/src/AbcCommon.hpp %buildroot%_includedir/coin/

#for i in %oname-driver clp; do
#	chrpath -r %mpidir/lib %buildroot%_bindir/$i
#done
chrpath -r %mpidir/lib %buildroot%_bindir/clp

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

%files
%_bindir/clp

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc %oname/examples/Makefile %oname/examples/*.c* %oname/examples/*.hpp
%doc %oname/examples/*.tiny %oname/examples/input.*
#_bindir/*driver

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%changelog
* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.16.10-alt1
- Updated to stable upstream version 1.16.10.

* Tue Feb 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.15.5-alt1.svn20140507.1
- build fixed
- gcc set to 4.9, docs not packaged

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.5-alt1.svn20140507
- New snapshot

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.5-alt1.svn20131130
- Version 1.15.5

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.2-alt1.svn20130831
- Version 1.15.2

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.8-alt1.svn20130202
- Version 1.14.8

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.7-alt2.svn20120830
- Rebuilt with glpk 4.48

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.7-alt1.svn20120830
- Version 1.14.7

* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.6-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.6-alt1.svn20120128
- Version 1.14.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.1-alt2.svn20110903
- Fixed RPATH

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.1-alt1.svn20110903
- Version 1.14.1

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.svn20110417
- Version 1.14

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.0-alt1.svn20101205.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.0-alt1.svn20101205.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.0-alt1.svn20101205
- Version 1.13.0

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.svn20100831.2
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.svn20100831.1
- Fixed linking of libraries

* Wed Sep 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.svn20100831
- Initial build for Sisyphus

