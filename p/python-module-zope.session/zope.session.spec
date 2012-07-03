%define oname zope.session
Name: python-module-%oname
Version: 3.9.5
Release: alt1
Summary: Client identification and sessions for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

Requires: python-module-zope.i18nmessageid
%py_requires ZODB3 zope.component zope.interface zope.location
%py_requires zope.publisher zope.minmax

%description
This package provides interfaces for client identification and session
support and their implementations for zope.publisher's request objects.

%package tests
Summary: Tests for zope.session
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides interfaces for client identification and session
support and their implementations for zope.publisher's request objects.

This package contains tests for zope.session.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.5-alt1
- Version 3.9.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.4-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt1
- Initial build for Sisyphus

