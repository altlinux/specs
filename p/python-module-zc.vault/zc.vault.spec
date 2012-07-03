%define oname zc.vault
Name: python-module-%oname
Version: 0.11
Release: alt2.1
Summary: Low-level versioning support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.vault/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc rwproperty zc.copy zc.freeze zc.objectlog
%py_requires zc.relationship zc.shortcut ZODB3 zope.app.container
%py_requires zope.app.intid zope.app.keyreference zope.cachedescriptors
%py_requires zope.component zope.copypastemove zope.event zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.proxy zope.publisher zope.schema
%py_requires zope.traversing

%description
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

%package tests
Summary: Tests for Low-level versioning support
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction zope.annotation zope.app.component
%py_requires zope.app.folder zope.app.testing zope.testing

%description tests
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

This package contains tests for Low-level versioning support.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

