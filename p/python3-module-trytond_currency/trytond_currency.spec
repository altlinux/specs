%define _unpackaged_files_terminate_build 1
%define oname trytond_currency

Name: python3-module-%oname
Version: 6.2.0
Release: alt1

Summary: Tryton module with currencies
License: GPL
Group: Development/Python3
Url: http://crd.lbl.gov/~dhbailey/mpdist/
BuildArch: noarch

Source0: https://files.pythonhosted.org/packages/5a/d3/97635ff5dfb7d90fbd9a3578f3d7e069b6ebf8fd9f553fa409e51f696f12/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


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
%python3_build

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
* Fri Mar 25 2022 Danil Shein <dshein@altlinux.org> 6.2.0-alt1
- Version updated to 6.2.0

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

