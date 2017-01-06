%define oname aiocouchdb

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.1
Release: alt1
Summary: CouchDB client built on top of aiohttp
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiocouchdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kxepal/aiocouchdb.git
Source0: https://pypi.python.org/packages/d6/a7/8448c45766dab455a3e08c6f6a09c1142ec6c89bd0a05b6c9eb99e3bd16a/aiocouchdb-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-oauthlib python-module-nose
#BuildPreReq: python-module-aiohttp python-module-trollius
#BuildPreReq: python-module-flake8
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-oauthlib python3-module-nose
#BuildPreReq: python3-module-aiohttp python3-module-asyncio
#BuildPreReq: python3-module-flake8
%endif

%py_provides %oname
%py_requires trollius oauthlib aiohttp

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-mccabe python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface python3-pyflakes python3-tools-pep8
BuildRequires: python3-module-flake8 python3-module-nose python3-module-pycrypto rpm-build-python3

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
%py3_requires asyncio oauthlib aiohttp

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
%setup -q -n aiocouchdb-%{version}

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
#make check
nosetests -v --with-doctest %oname
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#sed -i 's|nosetests|nosetests3|g' Makefile
#sed -i 's|which flake8|which python3-flake8|g' Makefile
#make check
nosetests3 -v --with-doctest %oname
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst docs/v1
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/v1
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.dev0.git20150420.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.dev0.git20150420.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.dev0.git20150420
- Version 0.9.0.dev0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.dev0.git20141117
- Initial build for Sisyphus

