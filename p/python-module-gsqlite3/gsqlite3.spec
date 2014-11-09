%define oname gsqlite3

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20141107
Summary: A wrapper for 'sqlite3' to make it play better with 'gevent'
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/gsqlite3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gilesbrown/gsqlite3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-gevent
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-gevent
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3

%description
A gevent-ification of pysqlite3, including a SQLAlchemy dialect.

The module takes a simple approach of any potentiall long running
methods off to the gevent hub threadpool for execution.

This lets greenlet code perform parallel queries.

%package -n python3-module-%oname
Summary: A wrapper for 'sqlite3' to make it play better with 'gevent'
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3

%description -n python3-module-%oname
A gevent-ification of pysqlite3, including a SQLAlchemy dialect.

The module takes a simple approach of any potentiall long running
methods off to the gevent hub threadpool for execution.

This lets greenlet code perform parallel queries.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst demo*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst demo*
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141107
- Initial build for Sisyphus

