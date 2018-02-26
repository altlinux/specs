%define oname zc.security
Name: python-module-%oname
Version: 4.2.0
Release: alt2.1
Summary: Principal-searching UI for Zope 3 Pluggable Authentication
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zope.app.authentication zope.app.component
%py_requires zope.app.security zope.component zope.interface
%py_requires zope.security zope.testing

%description
This package provides some Zope 3 user interfaces for searching for
principals managed by the pluggable authentication utility.

%package tests
Summary: Tests for zc.security
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides some Zope 3 user interfaces for searching for
principals managed by the pluggable authentication utility.

This package contains tests for zc.security.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus

