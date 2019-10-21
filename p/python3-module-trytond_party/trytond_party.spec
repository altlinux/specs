%define oname trytond_party

Name: python3-module-%oname
Version: 5.2.1
Release: alt1

Summary: Tryton module with parties and addresses
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/trytond_party/

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python3-module-setuptools rpm-build-python3


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
%setup

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
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt1
- Version updated to 5.2.1
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

