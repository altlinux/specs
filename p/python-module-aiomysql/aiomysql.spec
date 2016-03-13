%define oname aiomysql

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150218.1
Summary: Library for accessing a MySQL database from the asyncio
License: MIT
Group: Development/Python
Url: https://github.com/aio-libs/aiomysql
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiomysql.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pymysql python-module-asyncio
BuildPreReq: python-module-SQLAlchemy python-module-flake8
BuildPreReq: python-module-nose python-module-coverage
%endif
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pymysql python3-module-asyncio
BuildPreReq: python3-module-SQLAlchemy python3-module-flake8
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires pymysql asyncio sqlalchemy

%description
aiomysql is a "driver" for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends and reuses most parts of PyMySQL.
aiomysql try to be like awesome aiopg library and preserve same api,
look and feel.

%package -n python3-module-%oname
Summary: Library for accessing a MySQL database from the asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires pymysql asyncio sqlalchemy

%description -n python3-module-%oname
aiomysql is a "driver" for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends and reuses most parts of PyMySQL.
aiomysql try to be like awesome aiopg library and preserve same api,
look and feel.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
aiomysql is a "driver" for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends and reuses most parts of PyMySQL.
aiomysql try to be like awesome aiopg library and preserve same api,
look and feel.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
aiomysql is a "driver" for accessing a MySQL database from the asyncio
(PEP-3156/tulip) framework. It depends and reuses most parts of PyMySQL.
aiomysql try to be like awesome aiopg library and preserve same api,
look and feel.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150218.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150218
- Version 0.0.2

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150204
- Initial build for Sisyphus

