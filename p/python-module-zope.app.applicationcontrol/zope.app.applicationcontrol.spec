%define oname zope.app.applicationcontrol
Name: python-module-%oname
Version: 3.5.10
Release: alt1
Summary: Zope applicationcontrol
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.applicationcontrol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.applicationcontrol zope.component
%py_requires zope.i18nmessageid zope.interface zope.location
%py_requires zope.security zope.size zope.traversing

%description
The application control instance is usually generated upon startup. This
package provides runtime information adapter for application control and
Zope version. Also provide a utility with methods for shutting down and
restarting the server.

%package tests
Summary: Tests for zope.app.applicationcontrol
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.appsetup zope.app.authentication
%py_requires zope.app.component zope.app.testing zope.app.zcmlfiles
%py_requires zope.login zope.publisher zope.securitypolicy
%py_requires zope.testbrowser

%description tests
The application control instance is usually generated upon startup. This
package provides runtime information adapter for application control and
Zope version. Also provide a utility with methods for shutting down and
restarting the server.

This package contains tests for zope.app.applicationcontrol.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.10-alt1
- Version 3.5.10

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.9-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.9-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.9-alt2
- Moved all tests into tests package

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.9-alt1
- Initial build for Sisyphus

