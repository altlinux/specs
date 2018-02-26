%define oname zc.catalog
Name: python-module-%oname
Version: 1.5
Release: alt2.1
Summary: Extensions to the Zope 3 Catalog
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 pytz zope.catalog zope.component zope.container
%py_requires zope.i18nmessageid zope.index zope.interface zope.publisher
%py_requires zope.schema zope.security

%description
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

%package tests
Summary: Tests for Extensions to the Zope 3 Catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.intid zope.keyreference zope.login zope.securitypolicy
%py_requires zope.testbrowser zope.testing

%description tests
zc.catalog is an extension to the Zope 3 catalog, Zope 3's indexing and
search facility. zc.catalog contains a number of extensions to the Zope
3 catalog, such as some new indexes, improved globbing and stemming
support, and an alternative catalog implementation.

This package contains tests for Extensions to the Zope 3 Catalog.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

