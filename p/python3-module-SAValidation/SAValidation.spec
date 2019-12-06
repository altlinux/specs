%define _unpackaged_files_terminate_build 1
%define oname SAValidation

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: Active Record like validation on SQLAlchemy declarative model objects
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/SAValidation/
BuildArch: noarch

Source0: https://pypi.python.org/packages/77/b9/b88e840e46266c99b3a35cfe77272302b6023ee2fa3d2d408ca873268b72/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python3-module-nosexcover
BuildRequires: python3-module-mock
BuildRequires: python3-module-SQLAlchemy
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-FormEncode
BuildRequires: python3-modules-sqlite3

%py3_provides savalidation
%py3_requires sqlalchemy dateutil formencode sqlite3


%description
SAValidation facilitates Active Record like validation on SQLAlchemy
declarative model objects.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
SAValidation facilitates Active Record like validation on SQLAlchemy
declarative model objects.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

