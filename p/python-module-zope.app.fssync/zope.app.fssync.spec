%define oname zope.app.fssync
Name: python-module-%oname
Version: 3.5
Release: alt2.1
Summary: Filesystem synchronization utility for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.fssync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires paramiko zope.dublincore zope.fssync zope.i18nmessageid
%py_requires zope.interface zope.proxy zope.testbrowser zope.traversing
%py_requires zope.xmlpickle zope.app.catalog zope.app.component
%py_requires zope.app.dtmlpage zope.app.file zope.app.folder
%py_requires zope.app.module zope.app.securitypolicy zope.app.zcmlfiles
%py_requires zope.app.zptpage

%description
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

%package tests
Summary: Tests for zope.app.fssync
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The FSSync project (zope.app.fssync) provides support for filesystem
synchronization of Zope3 content that resides in a ZODB. This package
defines a Web-based API with basic support for some standard zope.app
content types and the standard security policy.

This project is build on top of the more general zope.fssync package
which provides object serialization and deserialization tools. If you
need a pure Python API which is independent of the ZODB and the Zope3
security machinery you should look at zope.fssync.

This package contains tests for zope.app.fssync.

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
%exclude %python_sitelibdir/*/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*/*test*
%python_sitelibdir/*/*/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

