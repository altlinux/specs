%define oname pyramid_asyncio

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20150214
Summary: pyramid framework with asyncio 
License: BSD-derived
Group: Development/Python
Url: https://github.com/mardiros/pyramid_asyncio
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardiros/pyramid_asyncio.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-pyramid-tests
BuildPreReq: python-module-gunicorn python-module-aiohttp
BuildPreReq: python-module-pyramid_kvs python-module-asyncio_redis
BuildPreReq: python-modules-json
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-pyramid-tests
BuildPreReq: python3-module-gunicorn python3-module-aiohttp
BuildPreReq: python3-module-pyramid_kvs python3-module-asyncio_redis
%endif

%py_provides %oname
%py_requires asyncio pyramid gunicorn pyramid_kvs asyncio_redis json

%description
A lib that override pyramid to build asyncio web application.

Basically, it change views to asyncio coroutine.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A lib that override pyramid to build asyncio web application.

Basically, it change views to asyncio coroutine.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: pyramid framework with asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio pyramid gunicorn pyramid_kvs asyncio_redis json

%description -n python3-module-%oname
A lib that override pyramid to build asyncio web application.

Basically, it change views to asyncio coroutine.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A lib that override pyramid to build asyncio web application.

Basically, it change views to asyncio coroutine.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst COPYRIGHT LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst COPYRIGHT LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150214
- Initial build for Sisyphus

