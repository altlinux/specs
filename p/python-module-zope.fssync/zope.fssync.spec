%define oname zope.fssync
Name: python-module-%oname
Version: 3.5.2
Release: alt2.1
Summary: Filesystem synchronization utility for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.fssync/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.annotation zope.component zope.dottedname
%py_requires zope.filerepresentation zope.interface zope.lifecycleevent
%py_requires zope.location zope.proxy zope.traversing zope.xmlpickle

%description
This package provides filesystem synchronization utilities for Zope 3.
It is used by the zope.app.fssync package.

%package tests
Summary: Tests for zope.fssync
Group: Development/Python
Requires: %name = %version-%release
%py_requires ZODB3 zope.testing py

%description tests
This package provides filesystem synchronization utilities for Zope 3.
It is used by the zope.app.fssync package.

This package contains tests for zope.fssync.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

