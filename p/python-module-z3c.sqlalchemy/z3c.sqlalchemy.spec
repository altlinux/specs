%define oname z3c.sqlalchemy
Name: python-module-%oname
Version: 1.4.0
Release: alt2.1
Summary: A SQLAlchemy wrapper for Zope 2 and Zope 3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires SQLAlchemy zope.sqlalchemy zope.component zope.interface
%py_requires zope.testing zope.schema

%description
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

%package tests
Summary: Tests for z3c.sqlalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite zope.testing

%description tests
z3c.sqlalchemy is yet another wrapper around SQLAlchemy. The
functionality of the wrapper is basically focused on easy integration
with Zope 2 and Zope 3. The wrapper cares about connection handling,
optional transaction integration with Zope 2/3 and wrapper management
(caching, introspection). z3c.sqlalchemy gives you flexible control over
the mapper creation.

This package contains tests for z3c.sqlalchemy.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

