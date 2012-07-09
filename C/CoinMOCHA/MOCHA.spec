%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname MOCHA
Name: Coin%oname
Version: 1.0.0
Release: alt3.svn20091122
Summary: Matroid Optimization: Combinatorial Heuristics and Algorithms
License: Eclipse Public License v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/MOCHA
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/MOCHA/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel liblapack-devel
BuildPreReq: libgmp_cxx-devel %mpiimpl-devel

%description
MOCHA is a software package which contains algorithms and heuristics to
solve multicriteria matroid optimization problems. Beyond specific
algorithms and heuristics, our package also contains and uses matroid
(and related) data structures which can be used as a foundation for new
and old algorithms and heuristics.

%package docs
Summary: Documentation for COIN-OR MOCHA
Group: Documentation
BuildArch: noarch

%description docs
MOCHA is a software package which contains algorithms and heuristics to
solve multicriteria matroid optimization problems. Beyond specific
algorithms and heuristics, our package also contains and uses matroid
(and related) data structures which can be used as a foundation for new
and old algorithms and heuristics.

This package contains documentation for MOCHA.

%package instances
Summary: Examples and data for COIN-OR MOCHA
Group: Sciences/Mathematics
BuildArch: noarch

%description instances
MOCHA is a software package which contains algorithms and heuristics to
solve multicriteria matroid optimization problems. Beyond specific
algorithms and heuristics, our package also contains and uses matroid
(and related) data structures which can be used as a foundation for new
and old algorithms and heuristics.

This package contains examples and data for MOCHA.

%prep
%setup
rm -f *.m4

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

#autoreconf
%configure \
	--with-blas=-lgoto2 \
	--with-lapack=-llapack \
	--with-gmp=%prefix \
	--with-coin-instdir=%prefix
%make_build

doxygen doxydoc/doxygen.conf

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%_man3dir
install -m644 Doxydoc/man/man3/* %buildroot%_man3dir

install -d %buildroot%_datadir/%oname
cp -fR %oname/Instances %buildroot%_datadir/%oname/

#for i in %buildroot%_bindir/*; do
#	chrpath -r %mpidir/lib $i
#done

%files
%doc %oname/AUTHORS %oname/LICENSE %oname/README %oname/TODO
%_bindir/*

%files docs
%doc Doxydoc/html/*
%_man3dir/*
%exclude %_man3dir/Matrix.3*

%files instances
%_datadir/%oname

%changelog
* Mon Jul 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3.svn20091122
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.svn20091122
- Fixed build

* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122.5
- Fixed build

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122.4
- Avoid conflict with libtrilinos10-devel-doc

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122.1
- Rebuilt for debuginfo

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20091122
- Initial build for Sisyphus

