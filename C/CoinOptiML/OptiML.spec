%define somver 0
%define sover %somver.0.0

%define oname OptiML
Name: Coin%oname
Version: 1.0
Release: alt1.svn20090212.5
Summary: Optimization methods in Machine Learning
License: CPL v1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/OptiML/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/OptiML/trunk
Source: %oname-%version.tar.gz

BuildPreReq: gcc-c++ gcc-fortran
BuildPreReq: liblapack-goto-devel

%description
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

%package -n CoinSVM-QP
Summary: Support Vector Machines Quadratic Programming solver
Group: Sciences/Mathematics

%description -n CoinSVM-QP
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains SVM-QP (Support Vector Machines Quadratic
Programming solver) is a software package that solves 2-norm soft margin
support vector machine  classification problem.

%package -n libCoinSVM-QP
Summary: Shared libraries of Support Vector Machines Quadratic Programming solver
Group: System/Libraries

%description -n libCoinSVM-QP
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains shared libraries of SVM-QP (Support Vector
Machines Quadratic Programming solver) is a software package that solves
2-norm soft margin support vector machine  classification problem.

%package -n libCoinSVM-QP-devel
Summary: Development files of Support Vector Machines Quadratic Programming solver
Group: Development/Other
Requires: libCoinSVM-QP = %version-%release

%description -n libCoinSVM-QP-devel
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains development files of SVM-QP (Support Vector
Machines Quadratic Programming solver) is a software package that solves
2-norm soft margin support vector machine  classification problem.

%package -n CoinSVMPath
Summary: C++ extension of COIN-OR SVM-QP
Group: Sciences/Mathematics

%description -n CoinSVMPath
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains SVMPath, the C++ extension of SVM-QP. Additionally
to solving the SVM problem for a given value of parameter C, the C++
version includes the ability compute a path of optimal solutions for any
given range of parameter C.

%package -n CoinSVMPath-doc
Summary: Documentation for C++ extension of COIN-OR SVM-QP
Group: Documentation
BuildArch: noarch

%description -n CoinSVMPath-doc
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains documentation for SVMPath, the C++ extension of
SVM-QP.

%package -n CoinSVMPath-devel
Summary: Development files of COIN-OR SVMPath
Group: Sciences/Mathematics
BuildArch: noarch

%description -n CoinSVMPath-devel
Optimization for Machine learning, interior point, active set method and
parametric solvers for support vector machines, solver for the sparse
inverse covariance problem.

This package contains development files of SVMPath, the C++ extension of
SVM-QP. Additionally to solving the SVM problem for a given value of
parameter C, the C++ version includes the ability compute a path of
optimal solutions for any given range of parameter C.

%prep
%setup
rm -f SVM-QP-fortran/*.m4

%build
pushd SVM-QP-fortran
%autoreconf
%add_optflags %optflags_shared
%configure
%make_build
popd

pushd SVMPath-cpp
%make_build
popd

%install
pushd SVM-QP-fortran
%makeinstall_std
popd

install -m755 SVMPath-cpp/path_main %buildroot%_bindir
install -d %buildroot%_includedir/coin
install -p -m644 SVMPath-cpp/*.h %buildroot%_includedir/coin

mkdir -p %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
for i in libsvmqp; do
	ar x ../$i.a
	gfortran -shared * -Wl,-soname,$i.so.%somver \
		-o ../$i.so.%sover -llapack -lgoto2
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir %buildroot%_libdir/tmp

%files -n CoinSVM-QP
%doc SVM-QP-fortran/AUTHORS SVM-QP-fortran/COPYING SVM-QP-fortran/README
%_bindir/svmqp

%files -n libCoinSVM-QP
%_libdir/*.so.*

%files -n libCoinSVM-QP-devel
%doc SVM-QP-fortran/*.f SVM-QP-fortran/random*
%_libdir/*.so

%files -n CoinSVMPath
%doc SVMPath-cpp/AUTHORS SVMPath-cpp/COPYING
%doc SVMPath-cpp/*.par
%_bindir/path_main

%files -n CoinSVMPath-doc
%doc SVMPath-cpp/*.txt SVMPath-cpp/*.doc

%files -n CoinSVMPath-devel
%_includedir/*

%changelog
* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212.5
- Built with GotoBLAS2 instead of ATLAS

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212.4
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212.3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212.2
- Rebuilt for soname set-versions

* Mon Sep 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212.1
- Extracted documentation for CoinSVMPath into separate package

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20090212
- Initial build for Sisyphus

