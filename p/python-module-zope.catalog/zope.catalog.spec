%define oname zope.catalog
Name: python-module-%oname
Version: 3.8.2
Release: alt1
Summary: Cataloging and Indexing Framework for the Zope Toolkit
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.annotation zope.intid zope.component
%py_requires zope.container zope.index zope.interface
%py_requires zope.lifecycleevent zope.location zope.schema

%description
Catalogs provide management of collections of related indexes with a
basic search algorithm.

%package tests
Summary: Tests for zope.catalog
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.site

%description tests
Catalogs provide management of collections of related indexes with a
basic search algorithm.

This package contains tests for zope.catalog.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Version 3.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

