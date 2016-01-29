%define oname aiohttp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.15.3
Release: alt2.git20150425
Summary: http client/server for asyncio
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-module-objects.inv
BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-trollius python-module-nose
#BuildPreReq: python-module-gunicorn python-module-chardet
#BuildPreReq: python-module-flake8 python-module-coverage
#BuildPreReq: python-module-path 
#python-module-bumpversion
#BuildPreReq: python-module-Cython
%endif
BuildPreReq: python-module-sphinx-devel
#python-module-alabaster
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython python3-module-aiohttp python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-notebook
BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-nose
#BuildPreReq: python3-module-gunicorn python3-module-chardet
#BuildPreReq: python3-module-flake8 python3-module-coverage
#BuildPreReq: python3-module-path 
#python3-module-bumpversion
#BuildPreReq: python3-module-Cython
%endif

%py_provides %oname
#%py_requires trollius chardet

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
#%py3_requires asyncio chardet

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
nosetests -s -v ./tests/
%endif
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
sed -i 's|flake8|python3-flake8|' Makefile
nosetests3 -s -v ./tests/
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
* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 0.15.3-alt2.git20150425
- rebuild with cleaned build requires

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.3-alt1.git20150425
- Version 0.15.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20150217
- Version 0.14.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.git20150123
- Version 0.14.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus

