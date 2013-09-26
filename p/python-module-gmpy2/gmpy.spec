%define oname gmpy2

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1
Summary: GMP/MPIR, MPFR, and MPC interface
License: LGPL
Group: Development/Python
Url: http://code.google.com/p/gmpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel libgmp-devel libmpfr-devel libmpc-devel
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

%if_with python3
%package -n python3-module-%oname
Summary: General MultiPrecision arithmetic for Python 3
Group: Development/Python3

%description -n python3-module-%oname
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.
%endif

%package docs
Summary: Documentation and tests for GMPY
Group: Development/Documentation
BuildArch: noarch

%description docs
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

This package contains documentation and tests for GMPY.

%package pickles
Summary: Pickles for GMPY
Group: Development/Python

%description pickles
A C-coded Python extension module that wraps the GMP library to provide
to Python code fast multiprecision arithmetic (integer, rational, and
float), random number generation, advanced number-theoretical functions,
and more.

This package contains pickles for GMPY.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C docs pickle
%make -C docs html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python test/gmpy_test.py
rm -f test/*.pyc
%if_with python3
pushd ../python3
python3 test/gmpy_test.py
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html test*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0.0-alt2.b1.1
- Rebuild with Python-3.3

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.b1
- Rebuilt with gmp 5.0.5

* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.b1
- Version 2.0.0b1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.15-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1
- Version 1.15

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt1.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1
- Initial build for Sisyphus

