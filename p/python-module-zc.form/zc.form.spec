%define oname zc.form
Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: This package is a possibly temporary appendage used to hold extra browser widgets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc pytz zc.resourcelibrary zc.sourcefactory
%py_requires ZODB3 zope.annotation zope.app.principalannotation
%py_requires zope.app.catalog zope.app.form zope.app.pagetemplate
%py_requires zope.app.zapi zope.cachedescriptors zope.component
%py_requires zope.exceptions zope.formlib zope.i18n zope.i18nmessageid
%py_requires zope.index zope.interface zope.publisher zope.schema
%py_requires zope.app.security zope.app.appsetup zope.app.securitypolicy
%py_requires zope.app.testing zope.configuration zope.testing
%py_requires zope.traversing zope.app.component zope.app.zcmlfiles

%description
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

%package tests
Summary: Tests for zc.form
Group: Development/Python
Requires: %name = %version-%release

%description tests
The form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.app.form package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.

This package contains tests for zc.form.

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
%doc src/zc/form/*.txt *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2
- Removed setuptools from requirements

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

