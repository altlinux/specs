%define oname aiohttp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.13.1
Release: alt2.git20141231
Summary: http client/server for asyncio
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius python-module-nose
BuildPreReq: python-module-gunicorn python-module-chardet
BuildPreReq: python-module-flake8 python-module-coverage
BuildPreReq: python-module-path
%endif
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-nose
BuildPreReq: python3-module-gunicorn python3-module-chardet
BuildPreReq: python3-module-flake8 python3-module-coverage
BuildPreReq: python3-module-path
%endif

%py_provides %oname
%py_requires trollius

%description
http client/server for asyncio (PEP-3156).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: http client/server for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
http client/server for asyncio (PEP-3156).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
http client/server for asyncio (PEP-3156).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
http client/server for asyncio (PEP-3156).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%if_with python2
find -type f -name '*.py' -exec \
	sed -i 's|asyncio.streams|trollius.streams|g' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|import asyncio|import trollius|' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|from asyncio|from trollius|' '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

rm -f requirements*

%check
%if_with python2
python setup.py test
%make vtest
%endif
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
sed -i 's|flake8|python3-flake8|' Makefile
%make vtest
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus

