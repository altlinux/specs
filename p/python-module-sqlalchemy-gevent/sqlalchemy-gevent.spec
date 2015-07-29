%define oname sqlalchemy-gevent

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150702
Summary: SQLAlchemy dialect adaptor for gevent to work in non-blocking mode
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy-gevent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hkwi/sqlalchemy_gevent.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-gevent
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-gevent
%endif

%py_provides sqlalchemy_gevent
%py_requires sqlalchemy gevent

%description
SQLAlchemy dialect adaptor for gevent to work in non-blocking mode.

%if_with python3
%package -n python3-module-%oname
Summary: SQLAlchemy dialect adaptor for gevent to work in non-blocking mode
Group: Development/Python3
%py3_provides sqlalchemy_gevent
%py3_requires sqlalchemy gevent

%description -n python3-module-%oname
SQLAlchemy dialect adaptor for gevent to work in non-blocking mode.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150702
- Initial build for Sisyphus

