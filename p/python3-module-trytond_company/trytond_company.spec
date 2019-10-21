%define _unpackaged_files_terminate_build 1
%define oname trytond_company

Name: python3-module-%oname
Version: 5.2.0
Release: alt1

Summary: The company module of the Tryton application platform
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/trytond_company/

Source0: https://pypi.python.org/packages/20/a6/1580d8a0ddd9a9c03bc48f5a123365c10f9934989c0be7015003f3e5a98e/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildPreReq: python3-module-setuptools

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
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT LICENSE README.rst doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/*/tests


%changelog
* Thu Oct 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.0-alt1
- version updated to 5.2.0
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

