%define _unpackaged_files_terminate_build 1
%define oname trytond_country
Name: python-module-%oname
Version: 4.2.0
Release: alt1.1
Summary: Tryton module with countries
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_country/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/05/b3/cbdccb60bd8a8c3c290f0b5fd75b36005275e44e109bc745f57aa479c0b3/%{oname}-%{version}.tar.gz

BuildPreReq: python-module-setuptools python-module-trytond-tests
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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

