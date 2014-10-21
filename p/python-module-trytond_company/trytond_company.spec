%define oname trytond_company
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: The company module of the Tryton application platform
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_company/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-pytz
BuildPreReq: python-module-trytond python-module-trytond_party
BuildPreReq: python-module-trytond_currency
BuildPreReq: python-module-trytond_country

%description
Tryton module with companies and employees.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Tryton module with companies and employees.

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
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

