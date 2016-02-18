%define oname pint

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.dev0.git20141107.1
Summary: Physical quantities module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Pint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hgrecco/pint.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zest.releaser python-module-pyroma
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zest.releaser python3-module-pyroma
%endif

%py_provides %oname
%py_requires zest.releaser pyroma

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv python-module-pyroma python-module-setuptools-tests python-module-zest.releaser python3-module-html5lib python3-module-pyroma python3-module-setuptools-tests python3-module-sphinx python3-module-zest.releaser rpm-build-python3 time

%description
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Physical quantities module
Group: Development/Python3
%py3_provides %oname
%py3_requires zest.releaser pyroma

%description -n python3-module-%oname
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and to
different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to its modular design, you to extend (or even
rewrite!) the complete list without changing the source code.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES* README bench
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testsuite
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/testsuite

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES* README bench
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testsuite

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testsuite
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.dev0.git20141107.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev0.git20141107
- Initial build for Sisyphus

