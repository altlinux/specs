%define oname zope.psycopgda
Name: python-module-%oname
Version: 1.1.1
Release: alt2.1
Summary: Psycopg Database Adapter for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.psycopgda/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component zope.interface zope.rdb zope.app.form

%description
This file outlines the basics of using Zope3 with PostgreSQL via
PsycopgDA.

%package tests
Summary: Tests for zope.psycopgda
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This file outlines the basics of using Zope3 with PostgreSQL via
PsycopgDA.

This package contains tests for zope.psycopgda.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

