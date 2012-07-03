%define oname zc.testbrowser
Name: python-module-%oname
Version: 1.0.0a5
Release: alt2.1
Summary: Programmable web browser for functional black-box testing of web applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc ClientForm mechanize simplejson zope.interface
%py_requires zope.schema

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
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt1
- Initial build for Sisyphus

