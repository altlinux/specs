%define oname zope.app.catalog
Name: python-module-%oname
Version: 3.8.1
Release: alt2.1
Summary: Management pages for Zope Catalog
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.catalog

%description
This package provides ZMI-based browser management pages and menu items
for zope.catalog - the cataloging and indexing framework for Zope 3.

%package tests
Summary: Tests for zope.app.catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component zope.app.intid
%py_requires zope.app.securitypolicy zope.app.testing zope.app.zcmlfiles
%py_requires zope.app.zptpage zope.login zope.publisher

%description tests
This package provides ZMI-based browser management pages and menu items
for zope.catalog - the cataloging and indexing framework for Zope 3.

This package contains tests for zope.app.catalog.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

