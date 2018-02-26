%define oname grokcore.viewlet
Name: python-module-%oname
Version: 1.9
Release: alt1
Summary: Grok-like configuration for zope viewlets
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.viewlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view martian zope.viewlet zope.contentprovider
%py_requires zope.browserpage zope.component zope.interface
%py_requires zope.publisher zope.security

%description
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

%package tests
Summary: Tests for grokcore.viewlet
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.appsetup zope.app.publication
%py_requires zope.app.wsgi zope.configuration zope.container
%py_requires zope.principalregistry zope.securitypolicy zope.site
%py_requires zope.testing zope.traversing

%description tests
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

This package contains tests for grokcore.viewlet.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Initial build for Sisyphus

