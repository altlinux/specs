%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname gmpy2

%def_with python3

Name: python-module-%oname
Version: 2.0.8
Release: alt1
Summary: GMP/MPIR, MPFR, and MPC interface
License: LGPL
Group: Development/Python
Url: http://code.google.com/p/gmpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/90/f4/9a2e384b325b69bc5827b9a6510a8fb4a51698c915c06a3f25a86458892a/%{oname}-%{version}.zip

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel libgmp-devel libmpfr-devel libmpc-devel
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libgmp-devel libmpfr-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: libmpc-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel rpm-build-python3 time

#BuildRequires: python3-devel
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
%setup -q -n %{oname}-%{version}
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
python test/runtests.py
rm -f test/*.pyc
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/gmpy_test.py
python3 test/runtests.py
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Version 2.0.5

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3

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

