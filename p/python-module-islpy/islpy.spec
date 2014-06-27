%define oname islpy
Name: python-module-%oname
Version: 2014.2
Release: alt1
Summary: Wrapper around isl, an integer set library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/islpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libisl-devel boost-python-devel libgmp-devel
BuildPreReq: gcc-c++ python-module-sphinx-bootstrap-theme
BuildPreReq: python-module-sphinx-devel

%description
islpy is a Python wrapper around Sven Verdoolaege's isl, a library for
manipulating sets and relations of integer points bounded by linear
constraints.

Supported operations on sets include

* intersection, union, set difference,
* emptiness check,
* convex hull,
* (integer) affine hull,
* integer projection,
* computing the lexicographic minimum using parametric integer
  programming,
* coalescing, and
* parametric vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%package pickles
Summary: Pickles for islpy
Group: Development/Python

%description pickles
islpy is a Python wrapper around Sven Verdoolaege's isl, a library for
manipulating sets and relations of integer points bounded by linear
constraints.

This package contains pickles for islpy.

%package doc
Summary: Documentation for islpy
Group: Development/Documentation
BuildArch: noarch

%description doc
islpy is a Python wrapper around Sven Verdoolaege's isl, a library for
manipulating sets and relations of integer points bounded by linear
constraints.

This package contains documentation for islpy.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
./configure.py \
	--boost-python-libname=boost_python \
	--cxxflags="-g"
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*

%changelog
* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1
- Initial build for Sisyphus

