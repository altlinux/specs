%define oname z3c.optionstorage
Name: python-module-%oname
Version: 1.0.7
Release: alt2.1
Summary: Optional Storages -- Persistent, Managable Vocabularies
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.optionstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.annotation zope.browserpage zope.component
%py_requires zope.configuration zope.i18n zope.interface zope.proxy
%py_requires zope.schema zope.security zope.traversing zope.app.form

%description
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

%package tests
Summary: Tests for z3c.optionstorage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Option Storages are vocabularies that store their values in the ZODB and
can be managed during application runtime.

This package contains tests for z3c.optionstorage.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus

