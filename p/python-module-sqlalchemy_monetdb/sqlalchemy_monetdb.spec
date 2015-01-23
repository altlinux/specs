%define oname sqlalchemy_monetdb

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9
Release: alt1
Summary: SQLAlchemy dialect for MonetDB
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy_monetdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-monetdb python-module-SQLAlchemy-tests
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-monetdb python3-module-SQLAlchemy-tests
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires monetdb sqlalchemy

%description
MonetDB dialect for SQLAlchemy.

%package -n python3-module-%oname
Summary: SQLAlchemy dialect for MonetDB
Group: Development/Python3
%py3_provides %oname
%py3_requires monetdb sqlalchemy

%description -n python3-module-%oname
MonetDB dialect for SQLAlchemy.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
python run_tests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 run_tests.py
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

