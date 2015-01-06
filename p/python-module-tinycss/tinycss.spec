%define oname tinycss

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140618
Summary: tinycss is a complete yet simple CSS parser for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tinycss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SimonSapin/tinycss.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: tinycss is a complete yet simple CSS parser for Python
Group: Development/Python3
%py_provides %oname

%description -n python3-module-%oname
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
tinycss is a complete yet simple CSS parser for Python. It supports the
full syntax and error handling for CSS 2.1 as well as some CSS 3
modules:

* CSS Color 3
* CSS Paged Media 3

It is designed to be easy to extend for new CSS modules and syntax, and
integrates well with cssselect for Selectors 3 support.

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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
python3 setup.py build_ext -i
py.test-%_python3_version -vv
popd
%endif

%files
%doc CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140618
- Initial build for Sisyphus

