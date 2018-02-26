%define oname zope.app.publication
Name: python-module-%oname
Version: 3.13.2
Release: alt1
Summary: Zope publication
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.publication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface ZODB3 zope.authentication zope.component
%py_requires zope.error zope.browser zope.location zope.publisher
%py_requires zope.traversing zope.app

%description
Publication and traversal components.

%package tests
Summary: Tests for Zope publication
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.appsetup zope.app.exception
%py_requires zope.app.http zope.app.wsgi zope.applicationcontrol
%py_requires zope.browserpage zope.login zope.password
%py_requires zope.principalregistry zope.security zope.securitypolicy
%py_requires zope.site

%description tests
Publication and traversal components.

This package contains tests for Zope publication.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.2-alt1
- Version 3.13.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.13.1-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt3
- Add necessary requirements

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt2
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.1-alt1
- Initial build for Sisyphus

