%define oname grokcore.xmlrpc
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: XML-RPC View Component for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.xmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view grokcore.traverser grokcore.content martian
%py_requires simplejson zope.component zope.interface zope.publisher

%description
This package provides base classes for XML-RPC Views for Grok.

%package tests
Summary: Tests for grokcore.xmlrpc
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.view zope.app.appsetup zope.app.wsgi
%py_requires zope.errorview zope.testing

%description tests
This package provides base classes for XML-RPC Views for Grok.

This package contains tests for grokcore.xmlrpc.

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
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

