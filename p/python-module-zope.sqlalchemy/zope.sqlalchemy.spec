%define oname zope.sqlalchemy
Name: python-module-%oname
Version: 0.7
Release: alt1
Summary: Minimal Zope/SQLAlchemy transaction integration
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope SQLAlchemy transaction zope.interface

%description
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

%package tests
Summary: Tests for zope.sqlalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite

%description tests
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it
seeks only to provide a data manager and makes no attempt to define a
zopeish way to configure engines.

For WSGI applications, Zope style automatic transaction management is
available with repoze.tm2, a part of Repoze BFG and Turbogears 2.

This package contains tests for zope.sqlalchemy.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

