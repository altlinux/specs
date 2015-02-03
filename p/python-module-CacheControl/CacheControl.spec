%define oname CacheControl

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.11.1
Release: alt1.git20150128
Summary: The httplib2 caching algorithms packaged up for use with requests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/CacheControl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionrock/cachecontrol.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-tox
BuildPreReq: python-module-pytest-cov python-module-mock
BuildPreReq: python-module-webtest python-module-redis-py
BuildPreReq: python-module-lockfile python-module-bumpversion
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-tox
BuildPreReq: python3-module-pytest-cov python3-module-mock
BuildPreReq: python3-module-webtest python3-module-redis-py
BuildPreReq: python3-module-lockfile python3-module-bumpversion
%endif

%py_provides cachecontrol
%py_requires requests redis lockfile

%description
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

It was written because httplib2's better support for caching is often
mitigated by its lack of threadsafety. The same is true of requests in
terms of caching.

%package -n python3-module-%oname
Summary: The httplib2 caching algorithms packaged up for use with requests
Group: Development/Python3
%py3_provides cachecontrol
%py3_requires requests redis lockfile

%description -n python3-module-%oname
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

It was written because httplib2's better support for caching is often
mitigated by its lack of threadsafety. The same is true of requests in
terms of caching.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test -vv --cov cachecontrol
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv --cov cachecontrol
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.git20150128
- Initial build for Sisyphus

