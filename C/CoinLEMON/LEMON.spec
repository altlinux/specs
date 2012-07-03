%define oname LEMON
%define sover 0
Name: Coin%oname
Version: 1.2.1
Release: alt1.hg20120203
Summary: Library for Efficient Modeling and Optimization in Networks
License: Boost Software License, Version 1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/LEMON.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://lemon.cs.elte.hu/hg/lemon
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCbc-devel
BuildPreReq: libgs-devel libCoinVol-devel cmake ghostscript-utils

Requires: lib%name = %version-%release

%description
LEMON stands for Library of Efficient Models and Optimization in
Networks. It is a C++ template library aimed at combinatorial
optimization tasks, especially those working with graphs and networks.

%package -n lib%name
Summary: Shared libraries of COIN-OR LEMON
Group: System/Libraries

%description -n lib%name
LEMON stands for Library of Efficient Models and Optimization in
Networks. It is a C++ template library aimed at combinatorial
optimization tasks, especially those working with graphs and networks.

This package contains shared libraries of COIN-OR LEMON.

%package -n lib%name-devel
Summary: Development files of COIN-OR LEMON
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
LEMON stands for Library of Efficient Models and Optimization in
Networks. It is a C++ template library aimed at combinatorial
optimization tasks, especially those working with graphs and networks.

This package contains development files of COIN-OR LEMON.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR LEMON
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
LEMON stands for Library of Efficient Models and Optimization in
Networks. It is a C++ template library aimed at combinatorial
optimization tasks, especially those working with graphs and networks.

This package contains development documentation for COIN-OR LEMON.

%package demo
Summary: Demo for COIN-OR LEMON
Group: Development/Documentation
BuildArch: noarch

%description demo
LEMON stands for Library of Efficient Models and Optimization in
Networks. It is a C++ template library aimed at combinatorial
optimization tasks, especially those working with graphs and networks.

This package contains demo for COIN-OR LEMON.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCOIN_INCLUDE_DIR:PATH="%_includedir/coin" \
	-DCOIN_ROOT_DIR:PATH=%prefix \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DSOVER:STRING=%sover \
	-DPROJECT_VERSION:STRING="%version" \
	-DGLPK_LIBS:STRING="-lglpk" \
	-DCLP_LIBS:STRING="-lOsiClp -lClp -lOsi" \
	-DCBC_LIBS:STRING="-lCbc -lCgl" \
%ifarch x86_64
	-DLIBSUFF:STRING=64 \
%endif
	.

%make_build

pushd doc
doxygen
popd

%install
%makeinstall_std

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/lemon

%files -n lib%name-devel-doc
%doc %_docdir/lemon/html/*

%files demo
%doc demo/*.cc demo/*.lgf demo/Makefile

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20120203
- New snapshot

* Sun Sep 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20110804
- New snapshot

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20110412
- New snapshot

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20101116.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20101116.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20101116.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.hg20101116
- Version 1.2.1

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20100622.1
- Rebuilt for soname set-versions

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20100622
- Initial build for Sisyphus

