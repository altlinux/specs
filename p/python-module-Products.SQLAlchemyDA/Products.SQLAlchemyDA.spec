%define oname Products.SQLAlchemyDA
Name: python-module-%oname
Version: 0.5.2
Release: alt1.dev.git20110122
Summary: A generic database adapter for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.SQLAlchemyDA/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.SQLAlchemyDA.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.sqlalchemy python-module-SQLAlchemy
BuildPreReq: python-module-zope.app.zapi
BuildPreReq: python-module-Products.ZSQLMethods

%py_provides %oname
Requires: python-module-Zope2
%py_requires z3c.sqlalchemy zope.app.zapi zope.component

%description
SQLAlchemyDA is a generic database adapter for ZSQL methods. Since it is
based on SQLAlchemy, SQLAlchemyDA supports all databases out-of-the box
that are supported by SQLAlchemy (Postgres, MySQL, Oracle, SQLite,
MS-SQL, Firebird, Informix).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.ZSQLMethods

%description tests
SQLAlchemyDA is a generic database adapter for ZSQL methods. Since it is
based on SQLAlchemy, SQLAlchemyDA supports all databases out-of-the box
that are supported by SQLAlchemy (Postgres, MySQL, Oracle, SQLite,
MS-SQL, Firebird, Informix).

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd Products/SQLAlchemyDA
cp -fR *.txt pt tests \
	%buildroot%python_sitelibdir/Products/SQLAlchemyDA/
popd

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.dev.git20110122
- Initial build for Sisyphus

