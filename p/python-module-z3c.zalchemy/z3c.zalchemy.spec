%define oname z3c.zalchemy
Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: SQLAlchemy integration into Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.zalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c SQLAlchemy ZODB3 zope.component zope.interface
%py_requires zope.schema zope.app.testing zope.app.component
%py_requires zope.app.keyreference zope.app.container
%py_requires zope.app.pagetemplate

%description
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

%package tests
Summary: Tests for z3c.zalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite

%description tests
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

This package contains tests for z3c.zalchemy.

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
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Version 0.2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt3.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt3
- Added necessary requirements

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Avoid conflict with python-module-z3c

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

