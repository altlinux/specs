%define oname aiocouchdb

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.7.0
Release: alt1.dev0.git20141117
Summary: CouchDB client built on top of aiohttp
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiocouchdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kxepal/aiocouchdb.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-oauthlib python-module-nose
BuildPreReq: python-module-aiohttp python-module-trollius
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-oauthlib python3-module-nose
BuildPreReq: python3-module-aiohttp python3-module-asyncio
%endif

%py_provides %oname
%py_requires trollius oauthlib

%description
CouchDB client built on top of aiohttp (asyncio).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
CouchDB client built on top of aiohttp (asyncio).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: CouchDB client built on top of aiohttp
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio oauthlib

%description -n python3-module-%oname
CouchDB client built on top of aiohttp (asyncio).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
CouchDB client built on top of aiohttp (asyncio).

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
%make check
%endif
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|g' Makefile
%make check
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.dev0.git20141117
- Initial build for Sisyphus

