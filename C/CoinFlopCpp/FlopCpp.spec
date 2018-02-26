%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname FlopCpp
Name: Coin%oname
Version: 1.1.2
Release: alt1.svn20120128
Summary: Formulation of Linear Optimization Problems in C++
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/FlopC++.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/FlopC++/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCgl-devel
BuildPreReq: libCoinOsi-devel libCoinCbc-devel libCoinSmi-devel
BuildPreReq: libCoinDyLP-devel libCoinSYMPHONY-devel %mpiimpl-devel

%description
An open source algebraic modelling language implemented as a C++ class
library.

Using FLOPC++, linear optimization models can be specified in a
declarative style, similar to algebraic modelling languages such as GAMS
and AMPL, within a C++ program. As a result the traditional strengths of
algebraic modelling languages are preserved, while embedding linear
optimization models in software applications is facilitated.

FLOPC++ can be used as a substitute for traditional modelling languages,
when modelling linear optimization problems, but its principal strength
lies in the fact that the modelling facilities are combined with a
powerful general purpose programming language. This combination is
essential for implementing efficient algorithms (using linear
optimization for subproblems), integrating optimization models in user
applications, etc.

%package -n lib%name
Summary: Shared libraries of COIN-OR FLOPC++
Group: System/Libraries

%description -n lib%name
An open source algebraic modelling language implemented as a C++ class
library.

Using FLOPC++, linear optimization models can be specified in a
declarative style, similar to algebraic modelling languages such as GAMS
and AMPL, within a C++ program. As a result the traditional strengths of
algebraic modelling languages are preserved, while embedding linear
optimization models in software applications is facilitated.

FLOPC++ can be used as a substitute for traditional modelling languages,
when modelling linear optimization problems, but its principal strength
lies in the fact that the modelling facilities are combined with a
powerful general purpose programming language. This combination is
essential for implementing efficient algorithms (using linear
optimization for subproblems), integrating optimization models in user
applications, etc.

This package contains shared libraries of COIN-OR FLOPC++.

%package -n lib%name-devel
Summary: Development files of COIN-OR FLOPC++
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
An open source algebraic modelling language implemented as a C++ class
library.

Using FLOPC++, linear optimization models can be specified in a
declarative style, similar to algebraic modelling languages such as GAMS
and AMPL, within a C++ program. As a result the traditional strengths of
algebraic modelling languages are preserved, while embedding linear
optimization models in software applications is facilitated.

FLOPC++ can be used as a substitute for traditional modelling languages,
when modelling linear optimization problems, but its principal strength
lies in the fact that the modelling facilities are combined with a
powerful general purpose programming language. This combination is
essential for implementing efficient algorithms (using linear
optimization for subproblems), integrating optimization models in user
applications, etc.

This package contains development files of COIN-OR FLOPC++.

%package examples
Summary: Examples for COIN-OR FLOPC++
Group: Development/Documentation
BuildArch: noarch

%description examples
An open source algebraic modelling language implemented as a C++ class
library.

Using FLOPC++, linear optimization models can be specified in a
declarative style, similar to algebraic modelling languages such as GAMS
and AMPL, within a C++ program. As a result the traditional strengths of
algebraic modelling languages are preserved, while embedding linear
optimization models in software applications is facilitated.

FLOPC++ can be used as a substitute for traditional modelling languages,
when modelling linear optimization problems, but its principal strength
lies in the fact that the modelling facilities are combined with a
powerful general purpose programming language. This combination is
essential for implementing efficient algorithms (using linear
optimization for subproblems), integrating optimization models in user
applications, etc.

This package contains examples for COIN-OR FLOPC++.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk \
	--with-sym-incdir=%_includedir/coin
export echo=echo
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

export echo=echo
%makeinstall_std

install -d %buildroot%_pkgconfigdir
cat <<EOF >%buildroot%_pkgconfigdir/flopcpp.pc
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir/coin

Name: FLOPC++
Description: COIN-OR FLOPC++
Version: %version
Libs: -lCoinUtils -lm
Cflags: -I%_includedir/coin
Requires: coinutils
EOF

rm -fR %buildroot%_docdir/coin

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc %oname/examples

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.svn20120128
- Version 1.1.2

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.svn20110825
- Fixed RPATH

* Sun Sep 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20110825
- Version 1.1.0

* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.6
- Fixed build

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.5
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.4
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.3
- Rebuilt with CoinBuildTools 0.6.1

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.2
- Fixed overlinking of libraries

* Mon Sep 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224.1
- Added pkg-config file

* Sat Sep 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20081224
- Initial build for Sisyphus

