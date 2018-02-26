%define oname z3c.resource
Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: Local resource container implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.resource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.proxy zope.annotation zope.app.component
%py_requires zope.app.container zope.app.generations zope.component
%py_requires zope.event zope.interface zope.lifecycleevent zope.location
%py_requires zope.publisher zope.traversing

%description
This package provides a local resource container implementation for
Zope3.

%package tests
Summary: Tests for z3c.resource
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.annotation z3c.testing zope.app.testing
%py_requires zope.publisher zope.testing

%description tests
This package provides a local resource container implementation for
Zope3.

This package contains tests for z3c.resource.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

