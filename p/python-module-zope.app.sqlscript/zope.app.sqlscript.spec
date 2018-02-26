%define oname zope.app.sqlscript
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: SQL Script -- Zope 3 Content Component
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.sqlscript/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.annotation zope.app.cache
%py_requires zope.app.component zope.app.form zope.component
%py_requires zope.container zope.documenttemplate zope.i18nmessageid
%py_requires zope.interface zope.rdb zope.schema zope.traversing

%description
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

%package tests
Summary: Tests for zope.app.sqlscript
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zptpage
%py_requires zope.app.zcmlfiles

%description tests
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

This package contains tests for zope.app.sqlscript.

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
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

