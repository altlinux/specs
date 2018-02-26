%define oname zope.app.locking
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Simple Object Locking Framework for Zope 3 applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.locking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.security zope.app.keyreference zope.app.i18n
%py_requires zope.interface zope.schema zope.component zope.app.i18n
%py_requires ZODB3 zope.event zope.traversing zope.size

%description
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

%package tests
Summary: Tests for zope.app.locking
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing zope.app.file zope.site

%description tests
This package provides a framework for object locking. The implementation
is intended to provide a simple general-purpose locking architecture
upon which other locking applications can be built (WebDAV locking, for
example).

This package contains tests for zope.app.locking.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

