%define oname zope.app.error
Name: python-module-%oname
Version: 3.5.3
Release: alt2.1
Summary: Error reporting utility management UI for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.error/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.component zope.error zope.publisher
%py_requires zope.traversing

%description
This package provides management views for the error reporting utility
defined in zope.error package.

%package tests
Summary: Tests for zope.app.error
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides management views for the error reporting utility
defined in zope.error package.

This package contains tests for zope.app.error.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

