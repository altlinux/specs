%define oname flask_sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1.git20141023
Summary: Adds SQLAlchemy support to your Flask application
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-SQLAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask python-module-SQLAlchemy
BuildPreReq: python-module-sphinx-devel flask-sphinx-themes
BuildPreReq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flask python3-module-SQLAlchemy
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname

%description
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

%package -n python3-module-%oname
Summary: Adds SQLAlchemy support to your Flask application
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/flask-sphinx-themes/* docs/_themes/

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
%doc AUTHORS CHANGES README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/_build/html

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20141023
- Initial build for Sisyphus

