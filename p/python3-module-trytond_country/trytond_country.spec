%define _unpackaged_files_terminate_build 1
%define oname trytond_country

Name: python3-module-%oname
Version: 6.2.1
Release: alt1
Summary: Tryton module with countries

License: GPL
Group: Development/Python3
Url: https://pypi.org/project/trytond-country
BuildArch: noarch

Source0: https://files.pythonhosted.org/packages/02/b4/4e8ee584437d3bef7bce36c3dd3a9b6def2a5d9fd9abfae51e51b5de91da/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%description
The country module of the Tryton application platform.

%package tests
Summary: Tryton module with countries
Group: Development/Python3
Requires: %name = %EVR

%description tests
The country module of the Tryton application platform.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT README.rst LICENSE doc/*
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/*/tests


%changelog
* Fri Mar 25 2022 Danil Shein <dshein@altlinux.org> 6.2.1-alt1
- Version updated to 6.2.1

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.4.0-alt1
- Version updated to 5.4.0.

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.0-alt1
- Version updated ti 5.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

