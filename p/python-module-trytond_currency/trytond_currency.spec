%define _unpackaged_files_terminate_build 1
%define oname trytond_currency
Name: python-module-%oname
Version: 4.2.0
Release: alt1.1
Summary: Tryton module with currencies
License: GPL
Group: Development/Python
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/14/b2/b636a2644d3f3401e6ec8e1618e2f669f3239d55359dacea7802df8ffbd1/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-trytond

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
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGELOG README doc/* COPYRIGHT PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

