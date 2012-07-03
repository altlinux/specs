%define oname zope.rdb
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Zope RDBMS transaction integration
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.rdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope transaction ZODB3 zope.container zope.interface
%py_requires zope.i18nmessageid zope.security zope.configuration
%py_requires zope.container zope.schema zope.thread

%description
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

%package tests
Summary: Tests for Zope RDBMS transaction integration
Group: Development/Python
Requires: %name = %version-%release

%description tests
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

This package contains tests for Zope RDBMS transaction integration.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

