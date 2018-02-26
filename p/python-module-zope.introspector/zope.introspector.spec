%define oname zope.introspector
Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: Introspection helpers for Zope and Python objects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.introspector/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope grokcore.component zope.interface zope.component
%py_requires zope.publisher martian

%description
Introspection helpers for Zope and Python objects.

%package tests
Summary: Tests for zope.introspector
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing z3c.testsetup
%py_requires zope.securitypolicy

%description tests
Introspection helpers for Zope and Python objects.

This package contains tests for zope.introspector.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

