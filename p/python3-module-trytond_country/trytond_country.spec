%define _unpackaged_files_terminate_build 1
%define oname trytond_country

Name: python3-module-%oname
Version: 5.2.0
Release: alt1
Summary: Tryton module with countries

License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/trytond_country/
BuildArch: noarch

Source0: https://pypi.python.org/packages/05/b3/cbdccb60bd8a8c3c290f0b5fd75b36005275e44e109bc745f57aa479c0b3/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
#python-module-trytond-tests


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
%python3_build_debug

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
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.0-alt1
- Version updated ti 5.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

