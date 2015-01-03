%define oname SAValidation
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Active Record like validation on SQLAlchemy declarative model objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SAValidation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-nose
BuildPreReq: python-module-nosexcover python-module-mock
BuildPreReq: python-module-SQLAlchemy python-module-dateutil
BuildPreReq: python-module-FormEncode python-modules-sqlite3

%py_provides savalidation
%py_requires sqlalchemy dateutil formencode sqlite3

%description
SAValidation facilitates Active Record like validation on SQLAlchemy
declarative model objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SAValidation facilitates Active Record like validation on SQLAlchemy
declarative model objects.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

