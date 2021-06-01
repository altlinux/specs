%define oname WebHelpers2

%def_disable check

Name: python3-module-%oname
Version: 2.0
Release: alt4.git20150117
Summary: Functions for web apps: generating HTML tags, showing results a pageful at a time, etc.
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/WebHelpers2/

# https://github.com/mikeorr/WebHelpers2.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-wheel
BuildRequires: python3-module-unidecode

%py3_provides webhelpers2
Provides: python3-module-webhelpers2 = %EVR

%description
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc CHANGELOG README.*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 2.0-alt4.git20150117
- Fixed Build Requires.
- Build without docs.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 2.0-alt3.git20150117
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0-alt2.git20150117.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.git20150117
- Version 2.0

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc3.git20150113
- Version 2.0rc3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc2.git20141111
- Version 2.0rc2

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc1.git20141005
- Initial build for Sisyphus

