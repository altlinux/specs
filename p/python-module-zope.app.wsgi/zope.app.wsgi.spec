%define oname zope.app.wsgi
Name: python-module-%oname
Version: 3.13.0
Release: alt4.1
Summary: WSGI application for the zope.publisher
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.wsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-ZODB3
%py_requires webtest ZConfig zope.app.appsetup zope.event
%py_requires zope.processlifetime zope.app.publication zope.interface
%py_requires zope.publisher zope.security zope.container zope.error
%py_requires zope.component zope.configuration zope.lifecycleevent
%py_requires zope.session zope.site zope.testbrowser zope.testing
%py_requires zope.traversing zope.app

%description
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

%package tests
Summary: Tests for zope.app.wsgi
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.authentication zope.browserpage
%py_requires zope.componentvocabulary zope.location zope.login
%py_requires zope.password zope.principalregistry zope.securitypolicy

%description tests
This package provides the WSGIPublisherApplication class which exposes
the object publishing machinery in zope.publisher as a WSGI application.

This package contains tests for zope.app.wsgi.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.0-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt3
- Disabled *.pth

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt2
- Added necessary requirements

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Initial build for Sisyphus

