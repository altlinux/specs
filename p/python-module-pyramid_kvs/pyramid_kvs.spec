%define oname pyramid_kvs

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150106
Summary: Session and cache for Pyramid
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid-kvs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Gandi/pyramid_kvs.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-redis-py
BuildPreReq: python-module-memcached python-module-nose
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-redis-py
BuildPreReq: python3-module-memcached python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires pyramid redis memcache

%description
Some Key Value Store basics for pyramid:

Two KVS are implemented:
- memcache
- redis

Here are the provides features:

- An application cache, shared by every request.
- A session manager
- A rate limit per session holder
- A perl session reader (except you are migrating a perl website,
  you probably don't want to use it).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing nose

%description tests
Some Key Value Store basics for pyramid:

Two KVS are implemented:
- memcache
- redis

Here are the provides features:

- An application cache, shared by every request.
- A session manager
- A rate limit per session holder
- A perl session reader (except you are migrating a perl website,
  you probably don't want to use it).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Session and cache for Pyramid
Group: Development/Python3
%py3_provides %oname
%py3_requires pyramid redis memcache

%description -n python3-module-%oname
Some Key Value Store basics for pyramid:

Two KVS are implemented:
- memcache
- redis

Here are the provides features:

- An application cache, shared by every request.
- A session manager
- A rate limit per session holder
- A perl session reader (except you are migrating a perl website,
  you probably don't want to use it).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing nose

%description -n python3-module-%oname-tests
Some Key Value Store basics for pyramid:

Two KVS are implemented:
- memcache
- redis

Here are the provides features:

- An application cache, shared by every request.
- A session manager
- A rate limit per session holder
- A perl session reader (except you are migrating a perl website,
  you probably don't want to use it).

This package contains tests for %oname.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150106
- Initial build for Sisyphus

