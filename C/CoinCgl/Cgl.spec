%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Cgl
Name: Coin%oname
Version: 0.59.9
Release: alt1
Summary: COIN-OR Cut Generation Library
License: EPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/Cgl

# https://www.coin-or.org/download/source/%oname/%oname-%version.tgz
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: libCoinUtils libglpk libCoinOsi libCoinClp
BuildRequires: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildRequires: libCoinUtils-devel libCoinClp-devel libCoinOsi-devel
BuildRequires: libCoinVol-devel chrpath
BuildRequires: libCoinDyLP-devel libnuma-devel

%description
The COIN-OR Cut Generation Library (Cgl) is an open collection of
cutting plane implementations ("cut generators") for use in teaching,
research, and applications. Cgl can be used with other COIN-OR packages
that make use of cuts, such as the mixed-integer linear programming
solver Cbc.

%package -n lib%name
Summary: Shared libraries of COIN-OR Cut Generation Library
Group: System/Libraries

%description -n lib%name
The COIN-OR Cut Generation Library (Cgl) is an open collection of
cutting plane implementations ("cut generators") for use in teaching,
research, and applications. Cgl can be used with other COIN-OR packages
that make use of cuts, such as the mixed-integer linear programming
solver Cbc.

This package contains shared libraries of COIN-OR Cut Generation
Library.

%package -n lib%name-devel
Summary: Development files of COIN-OR Cut Generation Library
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The COIN-OR Cut Generation Library (Cgl) is an open collection of
cutting plane implementations ("cut generators") for use in teaching,
research, and applications. Cgl can be used with other COIN-OR packages
that make use of cuts, such as the mixed-integer linear programming
solver Cbc.

This package contains development files of COIN-OR Cut Generation
Library.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Cut Generation Library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The COIN-OR Cut Generation Library (Cgl) is an open collection of
cutting plane implementations ("cut generators") for use in teaching,
research, and applications. Cgl can be used with other COIN-OR packages
that make use of cuts, such as the mixed-integer linear programming
solver Cbc.

This package contains development documentation for COIN-OR Cut
Generation Library.

%package examples
Summary: Examples for COIN-OR Cut Generation Library
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
The COIN-OR Cut Generation Library (Cgl) is an open collection of
cutting plane implementations ("cut generators") for use in teaching,
research, and applications. Cgl can be used with other COIN-OR packages
that make use of cuts, such as the mixed-integer linear programming
solver Cbc.

This package contains examples for COIN-OR Cut Generation Library.

%prep
%setup -n %oname-%version
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,Clp,CoinUtils,Data,Osi}

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-coin-instdir=%prefix \
	--with-dot \
	--disable-dependency-linking
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR
#make_build -C %oname/examples TOPDIR=$TOPDIR

pushd %oname/doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

install -p -m644 Cgl/src/CglZeroHalf/Cgl012cut.hpp \
	%buildroot%_includedir/coin/

#install -d %buildroot%_bindir
#install -m755 %oname/examples/cgl1 %buildroot%_bindir
#chrpath -r %mpidir/lib %buildroot%_bindir/cgl1

rm -fR %buildroot%_docdir/coin \
	%buildroot%_datadir/coin/doc

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc %oname/examples/*.cpp %oname/examples/Makefile
#_bindir/*

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%changelog
* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.59.9-alt1
- Updated to stable upstream version 0.59.9.

* Tue Feb 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.58.6-alt1.svn20140317.1
- build fixed
- gcc set to 4.9, docs not packaged

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.6-alt1.svn20140317
- Version 0.58.6

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.4-alt1.svn20131121
- Version 0.58.4

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.1-alt1.svn20130824
- Version 0.58.1

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.4-alt1.svn20130130
- Version 0.57.4

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.3-alt2.svn20120618
- New snapshot

* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.3-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.3-alt1.svn20120128
- Version 0.57.3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.0-alt2.svn20110814
- Fixed RPATH

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.0-alt1.svn20110814
- Version 0.57.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.56.2-alt1.svn20110417
- Version 0.56.2

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.56.0-alt1.svn20101005.1
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.56.0-alt1.svn20101005
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.56.0-alt1.svn20100831.2
- Version 0.56.0

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.55.0-alt1.svn20100831.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.55.0-alt1.svn20100831.1
- Fixed linking of libraries

* Wed Sep 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.55.0-alt1.svn20100831
- Initial build for Sisyphus

