%define oname islpy

%def_with python3

Name: python-module-%oname
Version: 2014.2
Release: alt2.1
Summary: Wrapper around isl, an integer set library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/islpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel libisl-devel boost-python-devel libgmp-devel
#BuildPreReq: gcc-c++ python-module-sphinx-bootstrap-theme
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel boost-python3-devel
#BuildPreReq: python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libstdc++-devel python-base python-devel python-module-Fabric python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-ecdsa python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-nose python-module-pycrypto python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: gcc-c++ python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-sphinx-bootstrap-theme python3-devel python3-module-setuptools rpm-build-python3 time

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

%package -n python3-module-%oname
Summary: Wrapper around isl, an integer set library
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export LC_ALL=en_US.UTF-8

./configure.py \
	--boost-python-libname=boost_python \
	--cxxflags="-g"
%python_build_debug

%if_with python3
pushd ../python3
./configure.py \
	--boost-python-libname=boost_python3 \
	--cxxflags="-g"
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2014.2-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1
- Initial build for Sisyphus

