%define oname zcontact
Name: python-module-%oname
Version: 0.1.0a11
Release: alt2.1
Summary: An online contact manager built on Zope 3
License: GPL v3
Group: Development/Python
Url: http://pypi.python.org/pypi/zcontact/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires paste.script zope.app.appsetup zope.app.authentication
%py_requires zope.app.component zope.app.container zope.app.error
%py_requires zope.app.form zope.app.publisher zope.app.publication
%py_requires zope.app.security zope.app.securitypolicy zope.app.twisted
%py_requires zope.app.wsgi zope.app.i18n zope.app.rotterdam
%py_requires zope.app.zcmlfiles zope.contentprovider zope.testbrowser
%py_requires docutils jquery.javascript jquery.layer z3c.form z3c.formjs
%py_requires z3c.formui z3c.layer z3c.pagelet z3c.template z3c.viewlet
%py_requires z3c.zrtresource z3c.menu.simple zope.viewlet

%description
ZContact is an online contact management application built on the Zope3
web application framework.

%package tests
Summary: Tests for zcontact
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip interfaces
%py_requires zope.testing zope.app.testing z3c.coverage

%description tests
ZContact is an online contact management application built on the Zope3
web application framework.

This package contains tests for zcontact.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*test*
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0a11-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0a11-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0a11-alt1
- Initial build for Sisyphus

