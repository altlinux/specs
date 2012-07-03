%define oname zope.app.zcmlfiles
Name: python-module-%oname
Version: 3.7.1
Release: alt1
Summary: Zope application server ZCML files
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.zcmlfiles
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.annotation zope.component zope.componentvocabulary
%py_requires zope.copypastemove zope.dublincore zope.formlib zope.i18n
%py_requires zope.location zope.publisher zope.size zope.traversing
%py_requires zope.app.applicationcontrol zope.app.appsetup
%py_requires zope.app.basicskin zope.app.broken zope.app.component
%py_requires zope.app.container zope.app.content zope.app.dependable
%py_requires zope.app.error zope.app.exception zope.app.folder
%py_requires zope.app.form zope.app.generations zope.app.http
%py_requires zope.app.i18n zope.app.locales zope.app.pagetemplate 
%py_requires zope.app.principalannotation zope.app.publication zope.app
%py_requires zope.app.publisher zope.app.rotterdam zope.app.schema 
%py_requires zope.app.security zope.app.wsgi zope.app.zopeappgenerations

%description
Zope application server ZCML files.

%package tests
Summary: Tests for zope.app.zcmlfiles
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Zope application server ZCML files.

This package contains tests for zope.app.zcmlfiles.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Disabled .pth
- Added necessary requirements

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

