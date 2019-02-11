%define oname islpy

%def_with python3
%def_without docs

Name: python-module-%oname
Version: 2018.2.1
Release: alt1
Summary: Wrapper around isl, an integer set library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/islpy

Source: %name-%version.tar

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pybind11
%endif

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pybind11

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-sphinx-bootstrap-theme
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
%endif


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

%if_with docs
prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
export LC_ALL=en_US.UTF-8

./configure.py \
	--cxxflags="-g"
%python_build_debug

%if_with python3
pushd ../python3
./configure.py \
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

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
make -C doc pickle
make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc README.rst
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 11 2019 Anton Midyukov <antohami@altlinux.org> 2018.2.1-alt1
- New version 2018.2.1
- without docs

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.2-alt2.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.2-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2014.2-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1
- Initial build for Sisyphus

