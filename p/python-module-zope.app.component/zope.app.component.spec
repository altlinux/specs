%define oname zope.app.component

%def_with python3

Name: python-module-%oname
Version: 3.9.3
Release: alt2.1
Summary: Local Zope Component Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.component/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: Local Zope Component Support
Group: Development/Python3
%py3_requires zope.site zope.annotation zope.app.container
%py3_requires zope.app.pagetemplate zope.cachedescriptors zope.component
%py3_requires zope.configuration zope.deprecation zope.event
%py3_requires zope.exceptions zope.filerepresentation zope.formlib
%py3_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py3_requires zope.publisher zope.schema zope.security zope.traversing
%py3_requires zope.componentvocabulary ZODB3

%description -n python3-module-%oname
NOTE: this package is deprecated. Its functionality has been moved to
more reusable packages, namely: zope.component, zope.security, zope.site
and zope.componentvocabulary. Please import from there instead.

This package provides various ZCML directives (view, resource) and a
user interface related to local component management.

%package -n python3-module-%oname-tests
Summary: Tests for Local Zope Component Support
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.schema zope.app.testing zope.app.zcmlfiles
%py3_requires zope.login zope.securitypolicy zope.testbrowser

%description -n python3-module-%oname-tests
NOTE: this package is deprecated. Its functionality has been moved to
more reusable packages, namely: zope.component, zope.security, zope.site
and zope.componentvocabulary. Please import from there instead.

This package provides various ZCML directives (view, resource) and a
user interface related to local component management.

This package contains tests for Local Zope Component Support.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.3-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.3-alt1
- Version 3.9.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Initial build for Sisyphus

