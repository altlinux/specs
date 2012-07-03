%define oname z3c.form
Name: python-module-%oname
Version: 2.5.1
Release: alt1
Summary: An advanced form and widget framework for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.form
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.browser zope.component zope.configuration
%py_requires zope.contentprovider zope.event zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.pagetemplate zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

%package tests
Summary: Tests for z3c.form
Group: Development/Python
Requires: %name = %version-%release
%py_requires lxml z3c.coverage z3c.template zc.sourcefactory
%py_requires zope.app.component zope.app.container zope.app.pagetemplate
%py_requires zope.app.security zope.app.testing zope.testing

%description tests
This package provides an implementation for HTML forms and widgets. The
goal is to provide a simple API but with the ability to easily customize
any data or steps.

This package contains tests for z3c.form.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus

