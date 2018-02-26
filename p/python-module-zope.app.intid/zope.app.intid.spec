%define oname zope.app.intid
Name: python-module-%oname
Version: 3.7.1
Release: alt2.1
Summary: ZMI views for Integer Id Utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.intid
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.intid zope.security zope.traversing

%description
This package provides browser views for adding and managing integer id
utility, provided by the zope.intid package.

%package tests
Summary: Tests for zope.app.intid
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.authentication zope.app.securitypolicy
%py_requires zope.app.testing zope.app.zcmlfiles zope.site zope.login
%py_requires zope.publisher

%description tests
This package provides browser views for adding and managing integer id
utility, provided by the zope.intid package.

This package contains tests for zope.app.intid.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

