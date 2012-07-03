%define somver 0
%define sover %somver.0.0
%define libname liboboe

%define oname OBOE
Name: Coin%oname
Version: 1.0.3
Release: alt3.svn20100530
Summary: COIN-OR Oracle Based Optimization Engine (OBOE)
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/OBOE/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/OBOE/trunk
Source: %oname-%version.tar.gz

BuildPreReq: doxygen graphviz libglpk-devel CoinBuildTools gcc-c++
BuildPreReq: libCoinUtils-devel liblapackpp-devel boost-devel
BuildPreReq: libCoinClp-devel libCoinOsi-devel

%description
OBOE (Oracle Based Optimization Engine) is an open source software for
general convex optimization. It assumes that a user-made code,
thereafter named oracle, is capable of delivering first order
information on the key elements of the problem (support the feasible
set, support to the objective function). The engine exploits this
information to construct the so-called localization set which is a
polyhedral approximation of the set of optimal solutions.

%package -n lib%name
Summary: Shared libraries of COIN-OR Oracle Based Optimization Engine (OBOE)
Group: System/Libraries

%description -n lib%name
OBOE (Oracle Based Optimization Engine) is an open source software for
general convex optimization. It assumes that a user-made code,
thereafter named oracle, is capable of delivering first order
information on the key elements of the problem (support the feasible
set, support to the objective function). The engine exploits this
information to construct the so-called localization set which is a
polyhedral approximation of the set of optimal solutions.

This package contains shared libraries of COIN-OR Oracle Based
Optimization Engine (OBOE).

%package -n lib%name-devel
Summary: Development files of COIN-OR Oracle Based Optimization Engine (OBOE)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
OBOE (Oracle Based Optimization Engine) is an open source software for
general convex optimization. It assumes that a user-made code,
thereafter named oracle, is capable of delivering first order
information on the key elements of the problem (support the feasible
set, support to the objective function). The engine exploits this
information to construct the so-called localization set which is a
polyhedral approximation of the set of optimal solutions.

This package contains development files of COIN-OR Oracle Based
Optimization Engine (OBOE).

%package -n lib%name-devel-doc
Summary: Documentation for COIN-OR Oracle Based Optimization Engine (OBOE)
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
OBOE (Oracle Based Optimization Engine) is an open source software for
general convex optimization. It assumes that a user-made code,
thereafter named oracle, is capable of delivering first order
information on the key elements of the problem (support the feasible
set, support to the objective function). The engine exploits this
information to construct the so-called localization set which is a
polyhedral approximation of the set of optimal solutions.

This package contains development documentation for COIN-OR Oracle Based
Optimization Engine (OBOE).

%prep
%setup

%build
./reconf
export LAPACKCPP_DIR=%prefix
export LAPACKCPP_LIB=-llapackpp
%configure \
	--with-osi-incdir=%_includedir/coin \
	--with-osi-lib=-lOsi \
	--with-glpk=yes \
	--with-glpk-incdir=%_includedir/glpk \
	--with-glpk-lib=-lglpk \
	--with-blas=-lgoto2 \
	--enable-serialization=yes
%make_build

doxygen

%install
%makeinstall_std

install -d %buildroot%_includedir/coin/oboe
mv %buildroot%_includedir/*.h %buildroot%_includedir/coin/oboe/

install -d %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
for i in ../*.a; do
	ar x $i
done
g++ -shared *.o -Wl,-soname,%libname.so.%somver \
	-o ../%libname.so.%sover -lOsiGlpk -lOsiClp -lCoinUtils -llapackpp \
	-llapack -lgoto2 -lboost_serialization-mt -lm
ln -s %libname.so.%sover ../%libname.so.%somver
ln -s %libname.so.%somver ../%libname.so
popd
rm -fR %buildroot%_libdir/tmp

%files -n lib%name
%doc AUTHORS CHANGES COPYING ChangeLog NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/html doc/*.html doc/userguide

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt3.svn20100530
- Rebuilt with Boost 1.49.0

* Fri Dec 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.svn20100530
- Rebuilt with Boost 1.48.0

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.6
- Rebuilt with Boost 1.47.0

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.5
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.4
- Rebuilt with Boost 1.46.1

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.3
- Rebuilt for debuginfo
- Rebuilt with Boost 1.46.0

* Mon Dec 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.2
- Rebuilt with Boost 1.45.0

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530.1
- Rebuilt for soname set-versions

* Sat Sep 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100530
- Initial build for Sisyphus

