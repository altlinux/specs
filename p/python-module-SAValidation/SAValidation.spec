%define _unpackaged_files_terminate_build 1
%define oname SAValidation
Name: python-module-%oname
Version: 0.4.1
Release: alt1.1
Summary: Active Record like validation on SQLAlchemy declarative model objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SAValidation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/77/b9/b88e840e46266c99b3a35cfe77272302b6023ee2fa3d2d408ca873268b72/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-nose
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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

