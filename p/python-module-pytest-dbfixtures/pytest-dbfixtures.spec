%define oname pytest-dbfixtures

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.git20141127.1.1
Summary: Databases fixtures plugin for py.test
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-dbfixtures/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ClearcodeHQ/pytest-dbfixtures.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-mirakuru python-module-pyaml
BuildPreReq: python-module-pymlconf python-module-path
BuildPreReq: python-module-mysqlclient python-module-psycopg2
BuildPreReq: python-module-pymongo python-module-elasticsearch
BuildPreReq: python-module-redis-py python-module-rabbitpy
BuildPreReq: python-module-pytest-cov python-module-pytest-xdist
BuildPreReq: python-module-coveralls python-module-pylama
BuildPreReq: python-module-port-for
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-mirakuru
BuildPreReq: python3-module-pymlconf python3-module-path
BuildPreReq: python3-module-mysqlclient python3-module-psycopg2
BuildPreReq: python3-module-pymongo python3-module-elasticsearch
BuildPreReq: python3-module-redis-py python3-module-rabbitpy
BuildPreReq: python3-module-pytest-cov python3-module-pytest-xdist
BuildPreReq: python3-module-coveralls python3-module-pylama
BuildPreReq: python3-module-port-for
%endif

%py_provides pytest_dbfixtures

%description
py.test clean fixtures for: postgresql, mysql, redis, mongo,
elasticsearch and rabbitmq.

Starts specific database deamon and cleanup all data produced during
tests.

%package -n python3-module-%oname
Summary: Databases fixtures plugin for py.test
Group: Development/Python3
%py3_provides pytest_dbfixtures

%description -n python3-module-%oname
py.test clean fixtures for: postgresql, mysql, redis, mongo,
elasticsearch and rabbitmq.

Starts specific database deamon and cleanup all data produced during
tests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
py.test clean fixtures for: postgresql, mysql, redis, mongo,
elasticsearch and rabbitmq.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
py.test clean fixtures for: postgresql, mysql, redis, mongo,
elasticsearch and rabbitmq.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.git20141127.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20141127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141127
- Version 0.8.0

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141117
- Version 0.7.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141106
- Version 0.6.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20141030
- Initial build for Sisyphus

