%define oname meta

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20120510
Summary: Framework to manipulate and analyze python ast's and bytecode
License: BSD-like
Group: Development/Python
Url: http://numba.pydata.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-python python-module-distribute
BuildPreReq: python-module-sphinx-devel

%description
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

%package tests
Summary: Tests for Meta
Group: Development/Python
Requires: %name = %EVR

%description tests
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains tests for Meta.

%package pickles
Summary: Pickles for Meta
Group: Development/Python

%description pickles
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains pickles for Meta.

%package docs
Summary: Documentation for Meta
Group: Development/Documentation

%description docs
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains documentation for Meta.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR _build/pickle %buildroot%python_sitelibdir/meta/

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.py*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc _build/html/*

%files tests
%python_sitelibdir/*/testing.py*
%python_sitelibdir/*/*/tests

%changelog
* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20120510
- Initial build for Sisyphus

