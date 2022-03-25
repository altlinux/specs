%define _unpackaged_files_terminate_build 1
%define oname trytond_party

Name: python3-module-%oname
Version: 6.2.0
Release: alt1

Summary: Tryton module with parties and addresses
License: GPL-3
Group: Development/Python3
Url: https://pypi.python.org/pypi/trytond_party/

Source0: https://files.pythonhosted.org/packages/18/e4/467603b1805ecd33a7a050665a4c713c7f753b8c90f1c7589d9ce4af3cdd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
The party module of the Tryton application platform.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The party module of the Tryton application platform.

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

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt1
- Version updated to 5.2.1
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

