%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: CoinMP
Version: 1.6.0
Release: alt2.svn20120128
Summary: C-API library that supports most of the functionality of CLP, CBC, and CGL projects
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/CoinMP.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/CoinMP/trunk
Source: %name-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCbc-devel
BuildPreReq: libCoinOsi-devel libCoinCgl-devel libCoinVol-devel
BuildPreReq: libCoinDyLP-devel libCoinSYMPHONY-devel %mpiimpl-devel
BuildPreReq: chrpath

%description
CoinMP is a C-API interface library that supports most of the
functionality of the CLP (Coin LP), CBC (Coin Branch-and-Cut), and CGL
(Cut Generation Library) projects.

%package -n lib%name
Summary: Shared libraries of CoinMP
Group: System/Libraries

%description -n lib%name
CoinMP is a C-API interface library that supports most of the
functionality of the CLP (Coin LP), CBC (Coin Branch-and-Cut), and CGL
(Cut Generation Library) projects.

This package contains shared libraries of CoinMP.

%package -n lib%name-devel
Summary: Development files of CoinMP
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
CoinMP is a C-API interface library that supports most of the
functionality of the CLP (Coin LP), CBC (Coin Branch-and-Cut), and CGL
(Cut Generation Library) projects.

This package contains development files of CoinMP.

%package examples
Summary: Examples for CoinMP
Group: Sciences/Mathematics
BuildArch: noarch

%description examples
CoinMP is a C-API interface library that supports most of the
functionality of the CLP (Coin LP), CBC (Coin Branch-and-Cut), and CGL
(Cut Generation Library) projects.

This package contains examples for CoinMP.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export echo=echo
%autoreconf
%configure

pushd %name
%autoreconf
%configure \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk
popd

%make_build
#make_build -C CoinMP/examples TOPDIR=$PWD

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export echo=echo
%makeinstall_std

#install -d %buildroot%_bindir
#install -m755 %name/examples/example \
#	%buildroot%_bindir/%name-example

#for i in %buildroot%_bindir/*; do
#	chrpath -d $i
#done

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %name/AUTHORS %name/LICENSE %name/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc %name/examples/*
#_bindir/*

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.svn20120128
- Rebuilt with OpenMPI 1.6

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.svn20120128
- Version 1.6.0

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20110807
- Fixed RPATH

* Tue Oct 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.svn20110807
- New snapshot

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.svn20110113
- Version 1.6

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20101017.2
- Added -g for compiler option

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20101017.1
- Rebuilt for debuginfo

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20101017
- New snapshot

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100207.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100207.1
- Fixed linking of libraries

* Fri Sep 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20100207
- Initial build for Sisyphus

