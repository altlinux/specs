%define _unpackaged_files_terminate_build 1
%define oname trytond_company
Name: python-module-%oname
Version: 4.2.0
Release: alt1.1
Summary: The company module of the Tryton application platform
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_company/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/20/a6/1580d8a0ddd9a9c03bc48f5a123365c10f9934989c0be7015003f3e5a98e/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-pytz
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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

