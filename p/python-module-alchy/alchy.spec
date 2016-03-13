%define oname alchy

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt1.git20150213.1
Summary: The declarative companion to SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/alchy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dgilland/alchy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-tox
BuildPreReq: python-tools-pep8 pylint python-module-pytest-cov
BuildPreReq: python-module-coveralls python-module-twine
BuildPreReq: python-module-wheel python-module-virtualenv
BuildPreReq: python-module-astroid
BuildPreReq: python-modules-sqlite3
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-tox
BuildPreReq: python3-tools-pep8 pylint-py3 python3-module-pytest-cov
BuildPreReq: python3-module-coveralls python3-module-twine
BuildPreReq: python3-module-wheel python3-module-virtualenv
BuildPreReq: python3-module-astroid
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname

%description
A SQLAlchemy extension for its declarative ORM that provides
enhancements for model classes, queries, and sessions.

%package -n python3-module-%oname
Summary: The declarative companion to SQLAlchemy
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A SQLAlchemy extension for its declarative ORM that provides
enhancements for model classes, queries, and sessions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python 

%description pickles
A SQLAlchemy extension for its declarative ORM that provides
enhancements for model classes, queries, and sessions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A SQLAlchemy extension for its declarative ORM that provides
enhancements for model classes, queries, and sessions.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
%make pytest
%if_with python3
pushd ../python3
sed -i 's|py\.test|py.test-%_python3_version|g' makefile
%make pytest
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1-alt1.git20150213.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20150213
- Version 1.5.1

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141216
- Version 1.5.0

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.git20141118
- Initial build for Sisyphus

