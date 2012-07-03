%define oname z3c.jsonrpc
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: JSON RPC server and client implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jsonrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.json zope.app.publication zope.component
%py_requires zope.configuration zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.location zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
This package provides an JSON-RPC server implementation for Zope3.

%package tests
Summary: Tests for z3c.jsonrpc
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.app.testing zope.security
%py_requires zope.browserpage zope.principalregistry zope.testbrowser
%py_requires zope.testing zope.securitypolicy

%description tests
This package provides an JSON-RPC server implementation for Zope3.

This package contains tests for z3c.jsonrpc.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

