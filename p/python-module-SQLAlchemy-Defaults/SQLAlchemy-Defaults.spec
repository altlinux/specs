%define oname SQLAlchemy-Defaults

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt1.git20141230
Summary: Smart SQLAlchemy defaults for lazy guys, like me
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Defaults/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/sqlalchemy-defaults.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-SQLAlchemy
BuildPreReq: python-module-Pygments python-module-jinja2
BuildPreReq: python-module-docutils python-module-flexmock
BuildPreReq: python-module-psycopg2 python-module-pymysql
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-SQLAlchemy
BuildPreReq: python3-module-Pygments python3-module-jinja2
BuildPreReq: python3-module-docutils python3-module-flexmock
BuildPreReq: python3-module-psycopg2 python3-module-pymysql
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides sqlalchemy_defaults

%description
Smart SQLAlchemy defaults for lazy guys, like me.

%package -n python3-module-%oname
Summary: Smart SQLAlchemy defaults for lazy guys, like me
Group: Development/Python3
%py3_provides sqlalchemy_defaults

%description -n python3-module-%oname
Smart SQLAlchemy defaults for lazy guys, like me.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20141230
- Initial build for Sisyphus

