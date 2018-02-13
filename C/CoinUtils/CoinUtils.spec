%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: CoinUtils
Version: 2.10.13
Release: alt1.1.1
Summary: Open-source collection of classes and functions for COIN-OR project
License: EPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/CoinUtils

# https://www.coin-or.org/download/source/%name/%name-%version.tgz
Source: %name-%version.tar
Patch1: %name-%version-alt-build.patch

BuildRequires(pre): %mpiimpl-devel
BuildRequires: CoinBuildTools gcc-c++ libglpk-devel
BuildRequires: liblapack-devel  zlib-devel bzlib-devel
BuildRequires: CoinSample-devel CoinNetlib-devel
BuildRequires: graphviz doxygen

%description
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

%package -n lib%name
Summary: Shared libraries of CoinUtils
Group: System/Libraries
Requires: CoinSample-data CoinNetlib-data

%description -n lib%name
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains shared libraries of CoinUtils.

%package -n lib%name-devel
Summary: Development files of CoinUtils
Group: Development/C++
Requires: lib%name = %version-%release
Requires: CoinSample-devel CoinNetlib-devel

%description -n lib%name-devel
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains development files of CoinUtils.

%package docs
Summary: Documentation for CoinUtils
Group: Development/Documentation
BuildArch: noarch

%description docs
The CoinUtils project is a collection of open-source utilities developed
and used by a variety of other projects in the COIN-OR repository. The
project includes classes for storing and manipulating sparse matrices
and vectors, performing matrix factorization, parsing input files in
standard formats, building representations of mathematical programs,
comparing floating point numbers with a tolerance, performing simple
presolve operations, and warm starting algorithms for mathematical
programs, among others.

This package contains development documentation for CoinUtils.

%prep
%setup
%patch1 -p1

# don't use bundled stuff
rm -rf {BuildTools,Data}

%build
mpi-selector --set %mpiimpl < /dev/null
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%autoreconf
%add_optflags -I%mpidir/include
%configure \
	--with-coin-instdir=%prefix \
	--with-glpk-lib=-lglpk \
	--with-glpk-incdir=%_includedir/glpk \
%ifarch mipsel
        --without-blas-lib \
%else
	--with-blas-lib=-lopenblas \
%endif
	--with-lapack-lib=-llapack \
	--with-dot \
	--disable-dependency-linking
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

pushd %name/doxydoc
doxygen doxygen.conf
popd

rm -fR %buildroot%_datadir/coin/doc \
	%buildroot%_docdir/coin

%files -n lib%name
%doc AUTHORS LICENSE
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files docs
%doc %name/doxydoc/doxydoc/html/*

%changelog
* Tue Feb 13 2018 Fr. Br. George <george@altlinux.ru> 2.10.13-alt1.1.1
- Fix mipsel build

* Mon Feb 12 2018 Fr. Br. George <george@altlinux.ru> 2.10.13-alt1.1
- Build for mipsel (without blas)

* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.13-alt1
- Updated to stable upstream version 2.10.13.

* Thu May 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.10-alt1.svn20140507
- New snapshot

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.10-alt1.svn20131125
- Version 2.9.10

* Wed Sep 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.4-alt2.svn20130909
- Rebuilt with glpk 4.52

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.4-alt1.svn20130909
- Version 2.9.4

* Wed Jul 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.2-alt1.svn20130419
- Version 2.9.2

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.8-alt2.svn20130203
- Built with %%autoreconf

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.8-alt1.svn20130203
- Version 2.8.8

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt2.svn20120901
- Rebuilt with glpk 4.48

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt1.svn20120901
- Version 2.8.7

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt4.svn20120129
- Built with OpenBLAS instead of GotoBLAS2

* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt3.svn20120129
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt2.svn20120129
- Fixed build

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.6-alt1.svn20120129
- Version 2.8.6

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.svn20110903
- Version 2.8.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.1-alt1.svn20110417
- Version 2.7.1

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205.1
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.svn20101205
- Version 2.7.0

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829.2
- Fixed overlinking of libraries

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829.1
- Fixed requirements

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.svn20100829
- Initial build for Sisyphus

