%define oname z3c.indexer
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: A new way to index objects for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.indexer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.catalog zope.container zope.intid zope.keyreference
%py_requires zope.cachedescriptors zope.component zope.deferredimport
%py_requires zope.event zope.index zope.interface zope.lifecycleevent
%py_requires zope.location zope.schema

%description
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

%package tests
Summary: Tests for z3c.indexer
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.testing zope.testing zope.keyreference
%py_requires zope.site

%description tests
This package provides a way to index objects and query indexes for
Zope3. This implementation is different from zope.catalog and is an
alternative to it.

This package contains tests for z3c.indexer.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

