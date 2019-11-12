%define oname pytest-dbfixtures

Name: python3-module-%oname
Version: 0.8.0
Release: alt2

Summary: Databases fixtures plugin for py.test
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-dbfixtures/
# https://github.com/ClearcodeHQ/pytest-dbfixtures.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mirakuru
BuildRequires: python3-module-pymlconf python3-module-path
BuildRequires: python3-module-mysqlclient python3-module-psycopg2
BuildRequires: python3-module-pymongo python3-module-elasticsearch
BuildRequires: python3-module-redis-py python3-module-rabbitpy
BuildRequires: python3-module-pytest-cov python3-module-pytest-xdist
BuildRequires: python3-module-coveralls python3-module-pylama
BuildRequires: python3-module-port-for python3-module-sphinx

%py3_provides pytest_dbfixtures


%description
py.test clean fixtures for: postgresql, mysql, redis, mongo,
elasticsearch and rabbitmq.

Starts specific database deamon and cleanup all data produced during
tests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.0-alt2
- disable python2

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

