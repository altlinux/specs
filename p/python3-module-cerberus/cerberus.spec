%define oname cerberus

Name: python3-module-%oname
Version: 1.3.2
Release: alt1
Summary: Extensible validation for Python dictionaries
License: ISCL
Group: Development/Python3
Url: https://pypi.python.org/pypi/Cerberus/

# https://github.com/pyeve/cerberus.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest

%py3_provides %oname

%description
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
py.test3 -v %oname/tests

%files
%doc AUTHORS LICENSE *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Tue Jul 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Build new version.
- Drop python2 support.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.2-alt2
- Fixed testing against Pytest 5.

* Sat Jul 14 2018 Terechkov Evgenii <evg@altlinux.org> 1.2-alt1
- 1.2 (ALT #35154)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt1.git20141120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20141120
- Initial build for Sisyphus

