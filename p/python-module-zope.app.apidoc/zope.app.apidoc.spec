%define oname zope.app.apidoc
Name: python-module-%oname
Version: 3.7.5
Release: alt2.1
Summary: API Documentation and Component Inspection for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.apidoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py_requires zope.app.basicskin zope.app.onlinehelp zope.app.preference
%py_requires zope.app.publisher zope.app.renderer zope.app.testing
%py_requires zope.app.tree zope.cachedescriptors zope.component
%py_requires zope.container zope.configuration zope.deprecation
%py_requires zope.i18n zope.site zope.hookable zope.interface
%py_requires zope.location zope.proxy zope.publisher zope.schema
%py_requires zope.security zope.testbrowser zope.testing zope.traversing

%description
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

%package tests
Summary: Tests for zope.app.apidoc
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.browserpage zope.securitypolicy zope.login

%description tests
This Zope 3 package provides fully dynamic API documentation of Zope 3
and registered add-on components. The package is very extensible and can
be easily extended by implementing new modules.

This package contains tests for zope.app.apidoc.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*
%python_sitelibdir/*/*/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.5-alt1
- Initial build for Sisyphus

