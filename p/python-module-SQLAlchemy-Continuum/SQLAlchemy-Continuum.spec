%define oname SQLAlchemy-Continuum

%def_with python3

Name: python-module-%oname
Version: 1.1.5
Release: alt1.git20141228
Summary: Versioning and auditing extension for SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Continuum/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/sqlalchemy-continuum.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-SQLAlchemy-Utils
BuildPreReq: python-module-anyjson python-module-flask
BuildPreReq: python-module-flask-login python-module-flask_sqlalchemy
BuildPreReq: python-module-flexmock python-module-SQLAlchemy-i18n
BuildPreReq: python-module-psycopg2 python-module-pymysql
BuildPreReq: python-module-six
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-SQLAlchemy-Utils
BuildPreReq: python3-module-anyjson python3-module-flask
BuildPreReq: python3-module-flask-login python3-module-flask_sqlalchemy
BuildPreReq: python3-module-flexmock python3-module-SQLAlchemy-i18n
BuildPreReq: python3-module-psycopg2 python3-module-pymysql
BuildPreReq: python3-module-six
%endif

%py_provides sqlalchemy_continuum
%py_requires flask

%description
Versioning and auditing extension for SQLAlchemy.

%package -n python3-module-%oname
Summary: Versioning and auditing extension for SQLAlchemy
Group: Development/Python3
%py3_provides sqlalchemy_continuum
%py3_requires flask

%description -n python3-module-%oname
Versioning and auditing extension for SQLAlchemy.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Versioning and auditing extension for SQLAlchemy.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Versioning and auditing extension for SQLAlchemy.

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

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1.git20141228
- Initial build for Sisyphus

