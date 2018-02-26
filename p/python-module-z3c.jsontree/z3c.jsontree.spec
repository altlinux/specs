%define oname z3c.jsontree
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: JSON RPC item tree for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jsontree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.json z3c.jsonrpc z3c.jsonrpcproxy z3c.template
%py_requires z3c.xmlhttp zope.component zope.container
%py_requires zope.contentprovider zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.proxy zope.publisher zope.security
%py_requires zope.traversing zope.viewlet

%description
This package provides an JSON-RPC item tree implementation for Zope3.

%package tests
Summary: Tests for JSON RPC item tree for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.testing zope.app.component zope.app.publication
%py_requires zope.app.testing zope.browsermenu zope.browserpage
%py_requires zope.browserresource zope.configuration zope.pagetemplate
%py_requires zope.principalregistry zope.security zope.site zope.testing
%py_requires zope.testbrowser

%description tests
This package provides an JSON-RPC item tree implementation for Zope3.

This package contains tests for JSON RPC item tree for Zope3.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

