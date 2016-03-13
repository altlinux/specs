%define oname pymbolic

%def_with python3

Name: python-module-%oname
Version: 2014.3
Release: alt1.git20141107.1.1
Summary: A package for symbolic computation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pymbolic
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/inducer/pymbolic.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-sphinx-devel
#BuildPreReq: python-module-setuptools-tests python-module-pytools-test
#BuildPreReq: python-module-decorator python-module-sympy
#BuildPreReq: python-module-sphinx-bootstrap-theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pytools-test
#BuildPreReq: python3-module-decorator python3-module-sympy
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-Fabric python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-decorator python-module-ecdsa python-module-future python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mpi4py python-module-mpmath python-module-nose python-module-numpy python-module-pycrypto python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sympy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-mpi4py python3-module-numpy python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-numpy-testing python-module-objects.inv python-module-pytools python-module-setuptools-tests python-module-sphinx-bootstrap-theme python-module-sympy-tests python3-module-future python3-module-mpmath python3-module-pytools python3-module-setuptools-tests rpm-build-python3 time

%description
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

%package -n python3-module-%oname
Summary: A package for symbolic computation
Group: Development/Python3

%description -n python3-module-%oname
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

%package pickles
Summary: Pickles for Pymbolic
Group: Development/Python

%description pickles
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

This package contains pickles for Pymbolic.

%package doc
Summary: Documentation for Pymbolic
Group: Development/Documentation
BuildArch: noarch

%description doc
Pymbolic is a small expression tree and symbolic manipulation library.
Two things set it apart from other libraries of its kind:

* Users can easily write their own symbolic operations, simply by
  deriving from the builtin visitor classes.
* Users can easily add their own symbolic entities to do calculations
  with.

Pymbolic currently understands regular arithmetic expressions,
derivatives, sparse polynomials, fractions, term substitution,
expansion. It automatically performs constant folding, and it can
compile its expressions into Python bytecode for fast(er) execution.

This package contains documentation for Pymbolic.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc LITERATURE README.rst TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.3-alt1.git20141107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2014.3-alt1.git20141107.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3-alt1.git20141107
- Version 2014.3
- Enabled testing

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt2
- Added module for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.2-alt1
- Version 2014.2

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.1.1-alt1
- Initial build for Sisyphus

