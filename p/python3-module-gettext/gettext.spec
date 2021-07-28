%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname gettext

Name: python3-module-%oname
Version: 3.0
Release: alt2
Summary: Python Gettext po to mo file compiler
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-gettext/

# https://github.com/hannosch/python-gettext.git
Source0: https://pypi.python.org/packages/80/a7/a4a5cf3aa9500dbb09b48dae6d4d9581883dd90ae7a84cbb2d3448410114/python-%{oname}-%{version}.zip
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-unittest2

%py3_provides pythongettext

%description
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

This package contains tests for %oname.

%prep
%setup -n python-%{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt2
- Drop python2 support.

* Sat Jul 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt1.2
- NMU: Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt1.dev.git20130210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev.git20130210
- Initial build for Sisyphus

