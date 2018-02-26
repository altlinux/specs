%define oname metslib
Name: CoinMETSlib
Version: 0.5.1
Release: alt1.svn20101103.2
Summary: Metaheuristics modeling framework and optimization toolkit
License: CPL v1.0 or GPL v3.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/metslib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/metslib/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel

%description
METSlib is an object oriented metaheuristics optimization framework and
toolkit in C++. Hill Climbing, Steepest Descent, Random Restart Local
Search, Variable Neighborhood Search, Iterated Local Search, Simulated
Annealing and Tabu Search algorithms are applicable to one unified
modeling framework.

%package -n lib%name
Summary: Shared libraries of COIN-OR METSlib
Group: System/Libraries

%description -n lib%name
METSlib is an object oriented metaheuristics optimization framework and
toolkit in C++. Hill Climbing, Steepest Descent, Random Restart Local
Search, Variable Neighborhood Search, Iterated Local Search, Simulated
Annealing and Tabu Search algorithms are applicable to one unified
modeling framework.

This package contains shared libraries of COIN-OR METSlib.

%package -n lib%name-devel
Summary: Development files of COIN-OR METSlib
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
METSlib is an object oriented metaheuristics optimization framework and
toolkit in C++. Hill Climbing, Steepest Descent, Random Restart Local
Search, Variable Neighborhood Search, Iterated Local Search, Simulated
Annealing and Tabu Search algorithms are applicable to one unified
modeling framework.

This package contains development files of COIN-OR METSlib.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR METSlib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
METSlib is an object oriented metaheuristics optimization framework and
toolkit in C++. Hill Climbing, Steepest Descent, Random Restart Local
Search, Variable Neighborhood Search, Iterated Local Search, Simulated
Annealing and Tabu Search algorithms are applicable to one unified
modeling framework.

This package contains development documentation for COIN-OR METSlib.

%prep
%setup

%build
./autogen.sh
%configure --enable-static=no
%make_build

doxygen doxydoc/doxygen.conf

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS COPYING* ChangeLog NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc doxydoc/html/*

%changelog
* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.svn20101103.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.svn20101103.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.svn20101103
- Version 0.5.1

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.svn20100526.1
- Rebuilt for soname set-versions

* Mon Sep 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.svn20100526
- Initial build for Sisyphus

