%define oname Active-SQLAlchemy

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20141128
Summary: A framework agnostic wrapper for SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Active-SQLAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardix/active-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-inflection python-module-SQLAlchemy
BuildPreReq: python-module-pymysql python-module-coverage
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-modules-json python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-inflection python3-module-SQLAlchemy
BuildPreReq: python3-module-pymysql python3-module-coverage
BuildPreReq: python3-module-pytest-cov python3-modules-sqlite3
BuildPreReq: python-tools-2to3
%endif

%py_provides active_sqlalchemy
%py_requires inflection sqlalchemy pymysql json

%description
Active-SQLAlchemy is a framework agnostic wrapper for SQLAlchemy that
makes it really easy to use by implementing a simple active record like
api, while it still uses the db.session underneath. Inspired by
Flask-SQLAlchemy.

%package -n python3-module-%oname
Summary: A framework agnostic wrapper for SQLAlchemy
Group: Development/Python3
%py3_provides active_sqlalchemy
%py3_requires inflection sqlalchemy pymysql

%description -n python3-module-%oname
Active-SQLAlchemy is a framework agnostic wrapper for SQLAlchemy that
makes it really easy to use by implementing a simple active record like
api, while it still uses the db.session underneath. Inspired by
Flask-SQLAlchemy.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141128
- Initial build for Sisyphus

