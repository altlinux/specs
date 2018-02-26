%define oname pyublas
Name: python-module-%oname
Version: 2011.1
Release: alt3.git20111202
Summary: Seamless Numpy-UBlas interoperability
License: BSD
Group: Development/Python
Url: http://mathema.tician.de/software/pyublas
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/pyublas.git
Source: %oname-%version.tar

BuildPreReq: boost-python-devel libnumpy-devel python-module-sphinx-devel
BuildPreReq: gcc-c++

%description
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

%package devel
Summary: Development files of PyUblas
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description devel
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains development files of PyUblas.

%package docs
Summary: Documentation for PyUblas
Group: Development/Documentation
BuildArch: noarch

%description docs
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains documentation for PyUblas.

%package pickles
Summary: Pickles for PyUblas
Group: Development/Python

%description pickles
PyUblas provides a seamless glue layer between Numpy and Boost.Ublas for
use with Boost.Python.

This package contains pickles for PyUblas.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%make -C doc html

%install
%python_install

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files devel
%doc test/*
%_includedir/*

%files docs
%doc doc/.build/html

%files pickles
%python_sitelibdir/%oname/pickle

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt3.git20111202
- Rebuilt with Boost 1.49.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20111202
- New snapshot

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt2.git20110405
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.1-alt1.git20110405.1.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405.1
- Rebuilt with Boost 1.47.0

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110405
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20110318
- Version 2011.1
- Enabled using Boost iterators

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020.2
- Rebuilt with python-module-sphinx-devel

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020.1
- Rebuilt with debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.1-alt1.git20101020
- Initial build for Sisyphus

