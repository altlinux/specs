%define oname requests-cache

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.8
Release: alt1.git20141219
Summary: Persistent cache for requests library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/reclosedev/requests-cache.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-unittest2
BuildPreReq: python-module-pymongo python-module-redis-py
BuildPreReq: python-modules-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-unittest2
BuildPreReq: python3-module-pymongo python3-module-redis-py
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides requests_cache
%py_requires sqlite3

%description
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%package -n python3-module-%oname
Summary: Persistent cache for requests library
Group: Development/Python3
%py3_provides requests_cache
%py3_requires sqlite3

%description -n python3-module-%oname
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst sandbox.py example.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst sandbox.py example.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20141219
- Initial build for Sisyphus

