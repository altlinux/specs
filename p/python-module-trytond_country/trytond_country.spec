%define oname trytond_country
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: Tryton module with countries
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_country/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-trytond-tests
BuildArch: noarch

%description
The country module of the Tryton application platform.

%package tests
Summary: Tests for %oname
Summary: Tryton module with countries
Group: Development/Python
Requires: %name = %EVR

%description tests
The country module of the Tryton application platform.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGELOG README doc/*
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

