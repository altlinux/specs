%define oname zc.testbrowser

Name: python3-module-%oname
Version: 1.0.0a5
Release: alt4

Summary: Programmable web browser for functional black-box testing of web applications
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zc.testbrowser/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires zc ClientForm mechanize simplejson zope.interface
%py3_requires zope.schema


%description
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

%package tests
Summary: Tests for zc.testbrowser
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

This package contains tests for zc.testbrowser.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0a5-alt4
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.0a5-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0a5-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0a5-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt1
- Initial build for Sisyphus

