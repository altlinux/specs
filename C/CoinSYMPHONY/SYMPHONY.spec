%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname SYMPHONY
%define somver 0
%define sover %somver.0.0
Name: Coin%oname
Version: 5.4.4
Release: alt1.svn20120204
Summary: Open-source solver for mixed-integer linear programs (MILPs) written in C
License: CPL v1.o
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/SYMPHONY.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/SYMPHONY/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel libCoinClp-devel libCoinCgl-devel
BuildPreReq: libCoinOsi-devel libCoinDyLP-devel libCoinVol-devel
BuildPreReq: libCoinCbc-devel
BuildPreReq: liblapack-devel
BuildPreReq: libreadline-devel %mpiimpl-devel chrpath
#BuildPreReq: texlive-latex-recommended

Requires: lib%name = %version-%release

%description
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

%package -n lib%name
Summary: Shared libraries of COIN-OR SYMPHONY
Group: System/Libraries

%description -n lib%name
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

This package contains shared libraries of COIN-OR SYMPHONY.

%package -n lib%name-devel
Summary: Development files of COIN-OR SYMPHONY
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

This package contains development files of COIN-OR SYMPHONY.

%package examples
Summary: Examples for COIN-OR SYMPHONY
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

This package contains examples for COIN-OR SYMPHONY.

%package applications-sources
Summary: Applications sources for COIN-OR SYMPHONY
Group: Sciences/Mathematics
BuildArch: noarch

%description applications-sources
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

This package contains applications sources for COIN-OR SYMPHONY.

%package doc
Summary: Documentation for COIN-OR SYMPHONY
Group: Documentation
BuildArch: noarch

%description doc
SYMPHONY is an open-source generic MILP solver, callable library, and
extensible framework for implementing customized solvers for
mixed-integer linear programs (MILPs).

This package contains documentation for COIN-OR SYMPHONY.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%add_optflags -pthread
%configure \
	--enable-static \
	--enable-shared=no \
	--with-coin-instdir=%prefix \
	--with-blas-lib=-lgoto2 \
	--with-lapack-lib=-llapack \
	--with-glpk-incdir=%_includedir/glpk \
	--enable-gnu-packages \
	--enable-sensitivity-analysis \
	--enable-draw-graph \
	--with-application
sed -i 's|\(wl=\).*|\1"-Wl,"|' libtool
cp -fR %oname/Examples ./
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR -C SYMPHONY/src libSym.la
%make_build TOPDIR=$TOPDIR

#make_build -C %oname/Examples TOPDIR=$TOPDIR

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

ln -s libSym.la SYMPHONY/src/.libs/libSym.lai
ln -s libSymAppl.la SYMPHONY/src/.libs/libSymAppl.lai
%makeinstall_std TOPDIR=$PWD

#for i in bicriteria milp milp2 sensitivity \
#	warm_start1 warm_start2 warm_start3
#do
#	chrpath -r %mpidir/lib %oname/Examples/$i
#	install -m755 %oname/Examples/$i %buildroot%_bindir/%oname-$i
#done

rm -fR %buildroot%_datadir/coin/doc \
	%buildroot%_docdir/coin

pushd %buildroot%_libdir
rm -f *.so*
for i in Sym OsiSym SymAppl; do
	mpicxx -shared -Wl,--whole-archive lib$i.a -Wl,--no-whole-archive \
		-L. $ADDLIB -lCgl -lOsiClp -lClp -lOsi -lCoinUtils \
		-o lib$i.so.%sover -Wl,-soname=lib$i.so.%somver -Wl,-z,defs
	ln -s lib$i.so.%sover lib$i.so.%somver
	ln -s lib$i.so.%somver lib$i.so
	ADDLIB="$ADDLIB -l$i"
done
popd

%files
%doc %oname/AUTHORS %oname/LICENSE %oname/README
%_bindir/symphony

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files examples
%doc Examples/*
#_bindir/*
#exclude %_bindir/symphony

%files applications-sources
%doc %oname/Applications %oname/Datasets

%files doc
%doc %oname/Doc/*

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.4-alt1.svn20120204
- Version 5.4.4

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt2.svn20110903
- Fixed RPATH

* Tue Oct 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt1.svn20110903
- Version 5.4.1

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.3-alt1.svn20110417
- Version 5.3.3

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1.svn20101209.3
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1.svn20101209.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1.svn20101209.1
- Rebuilt for debuginfo

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.1-alt1.svn20101209
- Version 5.3.1

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.4-alt1.svn20100818.2
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.4-alt1.svn20100818.1
- Fixed linking of libraries

* Fri Sep 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.4-alt1.svn20100818
- Initial build for Sisyphus

