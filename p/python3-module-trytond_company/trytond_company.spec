%define _unpackaged_files_terminate_build 1
%define oname trytond_company

Name: python3-module-%oname
Version: 6.2.0
Release: alt1

Summary: The company module of the Tryton application platform
License: GPL
Group: Development/Python3
Url: https://pypi.org/project/trytond-company

Source0: https://files.pythonhosted.org/packages/44/74/e264195515796a71df000e1cc0e70f958125bba8b536a58bf0809bc3e5b4/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: rpm-build-python3

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
%python3_build

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT LICENSE README.rst doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/*/tests


%changelog
* Fri Mar 25 2022 Danil Shein <dshein@altlinux.org> 6.2.0-alt1
- Version updated to 6.2.0

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.4.0-alt1
- Version updated to 5.4.0.

* Thu Oct 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.0-alt1
- version updated to 5.2.0
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

