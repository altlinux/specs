%define oname trytond_party
Name: python-module-%oname
Version: 3.4.0
Release: alt1.1
Summary: Tryton module with parties and addresses
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_party/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-sql
BuildPreReq: python-module-trytond python-module-trytond_country

%description
The party module of the Tryton application platform.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The party module of the Tryton application platform.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGELOG README doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

