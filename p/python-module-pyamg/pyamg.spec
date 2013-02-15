%define oname pyamg
Name: python-module-%oname
Version: 2.0.5
Release: alt2
Summary: PyAMG: Algebraic Multigrid Solvers in Python
License: BSD
Group: Development/Python
Url: http://code.google.com/p/pyamg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel gcc-c++
BuildPreReq: python-module-sphinx-devel python-module-scipy

%description
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

%package docs
Summary: Documentation for PyAMG
Group: Development/Documentation
BuildArch: noarch

%description docs
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains documentation for PyAMG.

%package pickles
Summary: Pickles for PyAMG
Group: Development/Python

%description pickles
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains pickles for PyAMG.

%package tests
Summary: Tests for PyAMG
Group: Development/Python
Requires: %name = %EVR

%description tests
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains tests for PyAMG.

%prep
%setup

%prepare_sphinx Docs
ln -s ../objects.inv Docs/source/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C Docs html
%make -C Docs pickle

cp -fR Docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/example*
%exclude %python_sitelibdir/*/pickle

%files docs
%doc Docs/build/html/*

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/testing
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/example*

%changelog
* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt2
- Moved examples into tests subpackage

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus

