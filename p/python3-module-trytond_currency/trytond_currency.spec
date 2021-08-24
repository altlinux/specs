%define _unpackaged_files_terminate_build 1
%define oname trytond_currency

Name: python3-module-%oname
Version: 5.4.0
Release: alt2

Summary: Tryton module with currencies
License: GPL
Group: Development/Python3
Url: http://crd.lbl.gov/~dhbailey/mpdist/
BuildArch: noarch

Source0: https://pypi.python.org/packages/14/b2/b636a2644d3f3401e6ec8e1618e2f669f3239d55359dacea7802df8ffbd1/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-module-setuptools


%description
The currency module of the Tryton application platform.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The currency module of the Tryton application platform.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT LICENSE README.rst doc/*
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/tests

%files tests
%python3_sitelibdir/*/*/*/tests


%changelog
* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt2
- s/python-module-setuptools//

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.4.0-alt1
- Version updated to 5.4.0.

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt1
- Version updated to 5.2.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

