%define oname zope.security
Name: python-module-%oname
Version: 4.0.0
Release: alt1.bzr20120517
Summary: Zope Security Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:zope.security
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-zope.proxy

Requires: python-module-zope.i18nmessageid
%py_requires zope.component zope.interface zope.location zope.proxy
%py_requires zope.schema

%description
The Security framework provides a generic mechanism to implement
security policies on Python objects.

%package tests
Summary: Tests for Zope Security Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains tests for Zope Security Framework.

%package examples
Summary: Examples for Zope Security Framework
Group: Development/Python
Requires: %name = %version-%release

%description examples
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains examples for Zope Security Framework.

%prep
%setup

%build
%python_build

%install
%python_install

touch src/zope/security/examples/__init__.py
cp -fR src/zope/security/examples \
	%buildroot%python_sitelibdir/zope/security/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/examples

%files tests
%python_sitelibdir/*/*/test*

%files examples
%python_sitelibdir/*/*/examples

%changelog
* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.bzr20120517
- Version 4.0.0dev

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Version 3.8.3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

