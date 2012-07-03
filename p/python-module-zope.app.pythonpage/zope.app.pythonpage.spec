%define oname zope.app.pythonpage
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: Python Page -- Zope 3 Content Components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.pythonpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.container zope.app.interpreter
%py_requires zope.interface zope.schema zope.app.i18n zope.security

%description
Python Page provides the user with a content object that interprets
Python in content space.

%package tests
Summary: Tests for zope.app.pythonpage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Python Page provides the user with a content object that interprets
Python in content space.

This package contains tests for zope.app.pythonpage.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

