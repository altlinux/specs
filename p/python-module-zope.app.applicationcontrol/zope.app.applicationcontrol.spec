%define oname zope.app.applicationcontrol

%def_with python3

Name: python-module-%oname
Version: 3.5.10
Release: alt2.1
Summary: Zope applicationcontrol
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.applicationcontrol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app zope.applicationcontrol zope.component
%py_requires zope.i18nmessageid zope.interface zope.location
%py_requires zope.security zope.size zope.traversing

%description
The application control instance is usually generated upon startup. This
package provides runtime information adapter for application control and
Zope version. Also provide a utility with methods for shutting down and
restarting the server.

%package -n python3-module-%oname
Summary: Zope applicationcontrol
Group: Development/Python3
%py3_requires zope.app zope.applicationcontrol zope.component
%py3_requires zope.i18nmessageid zope.interface zope.location
%py3_requires zope.security zope.size zope.traversing

%description -n python3-module-%oname
The application control instance is usually generated upon startup. This
package provides runtime information adapter for application control and
Zope version. Also provide a utility with methods for shutting down and
restarting the server.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.applicationcontrol
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.appsetup zope.app.authentication
%py3_requires zope.app.component zope.app.testing zope.app.zcmlfiles
%py3_requires zope.login zope.publisher zope.securitypolicy
%py3_requires zope.testbrowser

%description -n python3-module-%oname-tests
The application control instance is usually generated upon startup. This
package provides runtime information adapter for application control and
Zope version. Also provide a utility with methods for shutting down and
restarting the server.

This package contains tests for zope.app.applicationcontrol.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.10-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.10-alt2
- Added module for Python 3

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

