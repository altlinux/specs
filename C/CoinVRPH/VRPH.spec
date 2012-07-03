%define somver 0
%define sover %somver.0.0

%define oname VRPH
Name: Coin%oname
Version: 1.0.0
Release: alt2.svn20110727
Summary: Library of heuristics for generating solutions to Vehicle Routing Problems (VRPs)
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/VRPH
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/VRPH/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinOsi-devel libCoinSYMPHONY-devel
BuildPreReq: libplplot-devel

Requires: lib%name = %version-%release

%description
VRPH is an open source library of heuristics for the capacitated Vehicle
Routing Problem (VRP). It includes several example applications that can
be used to quickly generate good solutions to VRP instances containing
thousands of customer locations.

%package -n lib%name
Summary: Shared libraries of COIN-OR VRPH
Group: System/Libraries

%description -n lib%name
VRPH is an open source library of heuristics for the capacitated Vehicle
Routing Problem (VRP). It includes several example applications that can
be used to quickly generate good solutions to VRP instances containing
thousands of customer locations.

This package contains shared libraries of COIN-OR VRPH.

%package -n lib%name-devel
Summary: Development files of COIN-OR VRPH
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
VRPH is an open source library of heuristics for the capacitated Vehicle
Routing Problem (VRP). It includes several example applications that can
be used to quickly generate good solutions to VRP instances containing
thousands of customer locations.

This package contains development files of COIN-OR VRPH.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR VRPH
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
VRPH is an open source library of heuristics for the capacitated Vehicle
Routing Problem (VRP). It includes several example applications that can
be used to quickly generate good solutions to VRP instances containing
thousands of customer locations.

This package contains development documentation for COIN-OR VRPH.

%prep
%setup

%build
%make_build LIBDIR=%_libdir SOMVER=%somver SOVER=%sover \
	TOPDIR=$PWD

%make_build doc

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/coin

install -m755 bin/* %buildroot%_bindir
install -p -m644 inc/* %buildroot%_includedir/coin
cp -P lib/* %buildroot%_libdir/

%files
%doc AUTHORS LICENSE README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/html/*

%changelog
* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.svn20110727
- Rebuilt with plplot 5.9.9

* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20110727
- New snapshot

* Fri May 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20100413.3
- Rebuilt with plplot 5.9.7

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20100413.2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20100413.1
- Rebuilt for soname set-versions

* Thu Sep 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20100413
- Initial build for Sisyphus

