%define oname zope.app.i18n
Name: python-module-%oname
Version: 3.6.3
Release: alt2.1
Summary: Persistent translation domains and message catalogs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.publisher zope.component zope.container
%py_requires zope.configuration zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.security ZODB3

%description
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

%package tests
Summary: Tests for zope.app.i18n
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.component

%description tests
This package provides placeful persistent translation domains and
message catalogs along with ZMI views for managing them.

This package contains tests for zope.app.i18n.

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
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Initial build for Sisyphus

