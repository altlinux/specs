%define oname zope.introspectorui
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Views for the info objects from zope.introspector
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.introspectorui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope grokcore.component grokcore.view zope.interface
%py_requires zope.component zope.location zope.introspector
%py_requires z3c.autoinclude

%description
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

%package tests
Summary: Tests for zope.introspectorui
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing z3c.testsetup
%py_requires zope.securitypolicy

%description tests
zope.introspectorui is a set of views for the information objects
provided by zope.introspector.

This package contains tests for zope.introspectorui.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

