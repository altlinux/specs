Name: liblinear
Version: 1.93
Release: alt1
Summary: A Library for Large Linear Classification
License: BSD
Group: System/Libraries
Url: http://www.csie.ntu.edu.tw/~cjlin/liblinear/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libopenblas-devel

%description
LIBLINEAR is a linear classifier for data with millions of instances and
features. It supports

* L2-regularized classifiers
* L2-loss linear SVM, L1-loss linear SVM, and logistic regression (LR)
* L1-regularized classifiers (after version 1.4)
* L2-loss linear SVM and logistic regression (LR)
* L2-regularized support vector regression (after version 1.9)
* L2-loss linear SVR and L1-loss linear SVR.

%package devel
Summary: Development files of a library for Large Linear Classification
Group: Development/C++
Requires: %name = %version-%release

%description devel
LIBLINEAR is a linear classifier for data with millions of instances and
features. It supports

* L2-regularized classifiers
* L2-loss linear SVM, L1-loss linear SVM, and logistic regression (LR)
* L1-regularized classifiers (after version 1.4)
* L2-loss linear SVM and logistic regression (LR)
* L2-regularized support vector regression (after version 1.9)
* L2-loss linear SVR and L1-loss linear SVR.

This package contains development files of LIBLINEAR.

%package -n python-module-%name
Summary: Python interface for a library for Large Linear Classification
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description -n python-module-%name
LIBLINEAR is a linear classifier for data with millions of instances and
features. It supports

* L2-regularized classifiers
* L2-loss linear SVM, L1-loss linear SVM, and logistic regression (LR)
* L1-regularized classifiers (after version 1.4)
* L2-loss linear SVM and logistic regression (LR)
* L2-regularized support vector regression (after version 1.9)
* L2-loss linear SVR and L1-loss linear SVR.

This package contains python interface for LIBLINEAR.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_includedir/%name
install -d %buildroot%_libdir
install -d %buildroot%python_sitelibdir_noarch

install -m755 train predict %buildroot%_bindir
install -p -m644 *.h %buildroot%_includedir/%name
cp -P *.so* %buildroot%_libdir/
install -p -m644 python/*.py %buildroot%python_sitelibdir_noarch

%files
%doc README
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir_noarch/*

%changelog
* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.93-alt1
- Version 1.93

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.91-alt1
- Initial build for Sisyphus

