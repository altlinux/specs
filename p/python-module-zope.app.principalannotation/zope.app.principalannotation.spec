%define oname zope.app.principalannotation
Name: python-module-%oname
Version: 3.7.0
Release: alt2.1
Summary: Bootstrap subscriber and browser menu item for zope.principalannotation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.principalannotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires transaction zope.app.appsetup zope.processlifetime
%py_requires zope.principalannotation zope.app

%description
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

%package tests
Summary: Tests for zope.app.principalannotation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

This package contains tests for zope.app.principalannotation.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

