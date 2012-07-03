%define oname zope.app.component
Name: python-module-%oname
Version: 3.9.3
Release: alt1
Summary: Local Zope Component Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.component/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.site zope.annotation zope.app.container
%py_requires zope.app.pagetemplate zope.cachedescriptors zope.component
%py_requires zope.configuration zope.deprecation zope.event
%py_requires zope.exceptions zope.filerepresentation zope.formlib
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.publisher zope.schema zope.security zope.traversing
%py_requires zope.componentvocabulary ZODB3

%description
NOTE: this package is deprecated. Its functionality has been moved to
more reusable packages, namely: zope.component, zope.security, zope.site
and zope.componentvocabulary. Please import from there instead.

This package provides various ZCML directives (view, resource) and a
user interface related to local component management.

%package tests
Summary: Tests for Local Zope Component Support
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.schema zope.app.testing zope.app.zcmlfiles
%py_requires zope.login zope.securitypolicy zope.testbrowser

%description tests
NOTE: this package is deprecated. Its functionality has been moved to
more reusable packages, namely: zope.component, zope.security, zope.site
and zope.componentvocabulary. Please import from there instead.

This package provides various ZCML directives (view, resource) and a
user interface related to local component management.

This package contains tests for Local Zope Component Support.

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
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.3-alt1
- Version 3.9.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Initial build for Sisyphus

