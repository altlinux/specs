%define oname zope.app.cache
Name: python-module-%oname
Version: 3.7.0
Release: alt2.1
Summary: Zope Caching Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.annotation zope.app.form zope.app.pagetemplate
%py_requires zope.component zope.componentvocabulary zope.interface
%py_requires zope.proxy zope.publisher zope.ramcache zope.schema
%py_requires zope.traversing

%description
This package provides a caching mechanism for Zope applications.

%package tests
Summary: Tests for Zope Caching Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides a caching mechanism for Zope applications.

This package contains tests for Zope Caching Framework.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

