%define oname zope.app.homefolder
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: User Home Folders for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.homefolder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.form zope.app.security zope.i18nmessageid
%py_requires zope.container zope.dottedname zope.interface zope.schema
%py_requires zope.security zope.traversing

%description
The principal home folder subscriber lets you assign home folders to
principals as you would do in any OS. This particular implementation of
such a feature is intended as a demo of the power of the way to handle
principals and not as the holy grail. If you have concerns about the
assumptions made in this implementation (which are probably legitimate),
just ignore this package altogether.

%package tests
Summary: Tests for zope.app.homefolder
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.file zope.app.folder
%py_requires zope.app.securitypolicy zope.app.testing zope.testing

%description tests
The principal home folder subscriber lets you assign home folders to
principals as you would do in any OS. This particular implementation of
such a feature is intended as a demo of the power of the way to handle
principals and not as the holy grail. If you have concerns about the
assumptions made in this implementation (which are probably legitimate),
just ignore this package altogether.

This package contains tests for zope.app.homefolder.

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

