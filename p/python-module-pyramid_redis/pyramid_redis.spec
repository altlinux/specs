%define oname pyramid_redis

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20140929
Summary: Integrate Redis with a Pyramid web application
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_redis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thruflo/pyramid_redis.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-redis-py python-module-zope.component
BuildPreReq: python-module-zope.interface python-module-pyramid
BuildPreReq: python-module-nose python-module-zope.deprecation
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-redis-py python3-module-zope.component
BuildPreReq: python3-module-zope.interface python3-module-pyramid
BuildPreReq: python3-module-nose python3-module-zope.deprecation
%endif

%py_provides %oname
%py_requires zope.component zope.interface

%description
pyramid_redis is one specific way of integrating redis-py with a Pyramid
web application.

Features:

* provides a redis client at request.redis
* configurable per-process blocking connection pool

%package -n python3-module-%oname
Summary: Integrate Redis with a Pyramid web application
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.component zope.interface

%description -n python3-module-%oname
pyramid_redis is one specific way of integrating redis-py with a Pyramid
web application.

Features:

* provides a redis client at request.redis
* configurable per-process blocking connection pool

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.md UNLICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md UNLICENSE
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20140929
- Initial build for Sisyphus

