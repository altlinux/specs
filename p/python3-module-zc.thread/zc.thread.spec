%define oname zc.thread

Name: python3-module-%oname
Version: 0.1.0
Release: alt1.znanja1.git20120922.2
Summary: Thread-creation helper
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/zc.thread/

# https://github.com/znanja/zc.thread.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-mock
BuildPreReq: python3-module-zope.testing

%py3_provides %oname
%py3_requires zc

%description
This package provides a very simple thread-creation API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
This package provides a very simple thread-creation API.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt1.znanja1.git20120922.2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.znanja1.git20120922.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.znanja1.git20120922
- Initial build for Sisyphus

