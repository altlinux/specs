%define oname z3c.offlinepack
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Pack ZODB databases without running Zope or ZEO
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.offlinepack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.dottedname

%description
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

%package tests
Summary: Tests for z3c.offlinepack
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout zc.recipe.egg

%description tests
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

This package contains tests for z3c.offlinepack.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

