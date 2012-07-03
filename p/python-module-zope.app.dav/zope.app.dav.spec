%define oname zope.app.dav
Name: python-module-%oname
Version: 3.5.3
Release: alt2.1
Summary: Zope WebDAV Support (Basic)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.dav/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.annotation zope.container zope.app.file
%py_requires zope.app.form zope.component zope.configuration
%py_requires zope.dublincore zope.event zope.filerepresentation
%py_requires zope.interface zope.lifecycleevent zope.location
%py_requires zope.pagetemplate zope.publisher zope.schema zope.site
%py_requires zope.size zope.traversing

%description
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

%package tests
Summary: Tests for zope.app.dav
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.login

%description tests
This package provides basic WebDAV support for a Zope application. A
more advanced implementation is available in z3c.dav.

This package contains tests for zope.app.dav.

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

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

