%define oname trytond_currency
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: Tryton module with currencies
License: GPL
Group: Development/Python
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-trytond

%description
The currency module of the Tryton application platform.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The currency module of the Tryton application platform.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGELOG README TODO doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

