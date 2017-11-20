%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: CoinMP
Version: 1.8.3
Release: alt1
Summary: C-API library that supports most of the functionality of CLP, CBC, and CGL projects
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/CoinMP

# https://www.coin-or.org/download/source/%oname/%oname-%version.tgz
Source: %name-%version.tar
Patch1: %name-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildRequires: libCoinUtils-devel libCoinClp-devel libCoinCbc-devel
BuildRequires: libCoinOsi-devel libCoinCgl-devel libCoinVol-devel
BuildRequires: libCoinDyLP-devel libCoinSYMPHONY-devel
BuildRequires: chrpath libnuma-devel

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
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,Cbc,Cgl,Clp,CoinUtils,Data,Osi}

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure

pushd %name
%autoreconf
%configure \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk \
	--disable-dependency-linking
popd

%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

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

%changelog
* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.3-alt1
- Updated to upstream version 1.8.3.

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.7.6-alt1.svn20140107.1
- build fixed

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.6-alt1.svn20140107
- Version 1.7.6

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5-alt1.svn20131201
- Version 1.7.5

* Wed Sep 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.svn20130803
- Version 1.7.0

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

