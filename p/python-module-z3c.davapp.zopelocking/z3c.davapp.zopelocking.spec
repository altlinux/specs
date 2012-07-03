%define oname z3c.davapp.zopelocking
Name: python-module-%oname
Version: 1.0b1
Release: alt2.1
Summary: WebDAV locking support using zope.locking
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.davapp.zopelocking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.davapp z3c.dav zope.locking zope.app.keyreference
%py_requires zc.i18n

%description
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

%package tests
Summary: Tests for z3c.davapp.zopelocking
Group: Development/Python
Requires: %name = %version-%release
%py_requires cElementTree

%description tests
WebDAV locking support. Integrates the zope.locking package with z3c.dav
to provide locking functionality.

This package contains tests for z3c.davapp.zopelocking.

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
%exclude %python_sitelibdir/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

