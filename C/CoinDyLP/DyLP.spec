%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname DyLP
Name: Coin%oname
Version: 1.8.3
Release: alt1.svn20120128
Summary: COIN-OR dynamic simplex algorithm
License: CPL v1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/DyLP.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/DyLP/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinOsi-devel %mpiimpl-devel chrpath

%description
DyLP is an open-source implementation of the dynamic simplex algorithm
for linear programming. DyLP is pure C, heavily instrumented and
commented, targetted toward algorithm development. An OSI interface,
OsiDylp, is also available.

%package -n lib%name
Summary: Shared libraries of COIN-OR dynamic simplex algorithm
Group: System/Libraries

%description -n lib%name
DyLP is an open-source implementation of the dynamic simplex algorithm
for linear programming. DyLP is pure C, heavily instrumented and
commented, targetted toward algorithm development. An OSI interface,
OsiDylp, is also available.

This package contains shared libraries of DyLP.

%package -n lib%name-devel
Summary: Development files of COIN-OR dynamic simplex algorithm
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
DyLP is an open-source implementation of the dynamic simplex algorithm
for linear programming. DyLP is pure C, heavily instrumented and
commented, targetted toward algorithm development. An OSI interface,
OsiDylp, is also available.

This package contains development files of DyLP.

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR dynamic simplex algorithm
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
DyLP is an open-source implementation of the dynamic simplex algorithm
for linear programming. DyLP is pure C, heavily instrumented and
commented, targetted toward algorithm development. An OSI interface,
OsiDylp, is also available.

This package contains development documentation for DyLP.

%package examples
Summary: Examples for COIN-OR dynamic simplex algorithm
Group: Sciences/Mathematics
#Requires: lib%name = %version-%release
BuildArch: noarch

%description examples
DyLP is an open-source implementation of the dynamic simplex algorithm
for linear programming. DyLP is pure C, heavily instrumented and
commented, targetted toward algorithm development. An OSI interface,
OsiDylp, is also available.

This package contains examples for DyLP.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

SAMPLE=$(pkg-config coindatasample --variable=datadir)
%autoreconf
%configure \
	--enable-debug \
	--with-coin-instdir=%prefix \
	--with-dot \
	--with-sample-datadir=$SAMPLE
sed -i 's|\(wl\=\).*|\1"-Wl,"|g' libtool
TOPDIR=$PWD
%make_build TOPDIR=$TOPDIR MPIDIR=%mpidir
#make_build -C %oname/examples TOPDIR=$TOPDIR

pushd %oname/doxydoc
doxygen doxygen.conf
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD MPIDIR=%mpidir

#install -d %buildroot%_bindir
#install -m755 %oname/examples/*dylp %buildroot%_bindir
#install -m755 %oname/examples/plain %buildroot%_bindir/%oname-plain

#for i in %buildroot%_libdir/*.so %buildroot%_bindir/*dylp
for i in %buildroot%_libdir/*.so
do
	chrpath -r %mpidir/lib $i
done

rm -fR %buildroot%_datadir/coin/doc

%files -n lib%name
%doc %oname/AUTHORS %oname/LICENSE %oname/NEWS %oname/README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %oname/doxydoc/doxydoc/html/*

%files examples
%doc %oname/examples/*.spc %oname/examples/*.c*
%doc %oname/examples/README %oname/examples/Makefile
%doc %oname/src/Dylp/dy_errmsgs.txt
#_bindir/*

%changelog
* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1.svn20120128
- Version 1.8.3

* Sun Sep 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.svn20110814
- Version 1.8.0

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.svn20110417
- Version 1.7.2

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.svn20101205.2
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.svn20101205.1
- Rebuilt for debuginfo

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.svn20101205
- Version 1.7.0

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.svn20100829.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.svn20100829.1
- Fixed linking of libraries

* Wed Sep 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.svn20100829
- Initial build for Sisyphus

