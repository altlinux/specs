%define oname SQLAlchemy-Utils

%def_with python3

Name: python-module-%oname
Version: 0.28.3
Release: alt1.git20141217
Summary: Various utility functions for SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/sqlalchemy-utils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-SQLAlchemy
BuildPreReq: python-module-anyjson
BuildPreReq: python-module-babel python-module-arrow
BuildPreReq: python-module-intervals python-module-phonenumbers
BuildPreReq: python-module-passlib python-module-colour
BuildPreReq: python-module-ipaddr python-module-dateutil
BuildPreReq: python-module-furl python-module-cryptography
BuildPreReq: python-module-Pygments python-module-jinja2
BuildPreReq: python-module-docutils python-module-flexmock
BuildPreReq: python-module-psycopg2 python-module-pytz
BuildPreReq: python-module-pymysql
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-SQLAlchemy
BuildPreReq: python3-module-anyjson
BuildPreReq: python3-module-babel python3-module-arrow
BuildPreReq: python3-module-intervals python3-module-phonenumbers
BuildPreReq: python3-module-passlib python3-module-colour
BuildPreReq: python3-module-ipaddr python3-module-dateutil
BuildPreReq: python3-module-cryptography
BuildPreReq: python3-module-Pygments python3-module-jinja2
BuildPreReq: python3-module-docutils python3-module-flexmock
BuildPreReq: python3-module-psycopg2 python3-module-pytz
BuildPreReq: python3-module-pymysql
%endif

%py_provides sqlalchemy_utils

%description
Various utility functions and custom data types for SQLAlchemy.

%package -n python3-module-%oname
Summary: Various utility functions for SQLAlchemy
Group: Development/Python3
%py3_provides sqlalchemy_utils

%description -n python3-module-%oname
Various utility functions and custom data types for SQLAlchemy.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Various utility functions and custom data types for SQLAlchemy.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Various utility functions and custom data types for SQLAlchemy.

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
* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28.3-alt1.git20141217
- Version 0.28.3

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.8-alt1.git20141113
- Version 0.27.8

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.7-alt1.git20141103
- Version 0.27.7

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.6-alt1.git20141029
- Initial build for Sisyphus

