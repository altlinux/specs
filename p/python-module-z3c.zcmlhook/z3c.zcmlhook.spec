%define oname z3c.zcmlhook
Name: python-module-%oname
Version: 1.0b1
Release: alt2.1
Summary: Easily hook into the ZCML processing machinery
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.zcmlhook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.interface zope.schema
%py_requires zope.configuration

%description
This package provides means of hooking into the Zope (ZCML)
configuration process.

%package tests
Summary: Tests for z3c.zcmlhook
Group: Development/Python
Requires: %name = %version-%release
%py_requires nose

%description tests
This package provides means of hooking into the Zope (ZCML)
configuration process.

This package contains tests for z3c.zcmlhook.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1
- Initial build for Sisyphus

