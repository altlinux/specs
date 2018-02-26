%define oname z3c.language.negotiator
Name: python-module-%oname
Version: 1.1.3
Release: alt2.1
Summary: Zope3 i18n language negotiator
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.language.negotiator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.language.session zope.app.generations zope.component
%py_requires zope.container zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.publisher zope.schema

%description
This package provides a local implementation of the INegotiator
interface defined in zope.i18n.interfaces. The negotiator implementation
offers some additional usefull attributes which are explained later.
This INegotiator is also used in the z3c.language.switch package.

%package tests
Summary: Tests for Zope3 i18n language negotiator
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.testing z3c.coverage zope.testing

%description tests
This package provides a local implementation of the INegotiator
interface defined in zope.i18n.interfaces. The negotiator implementation
offers some additional usefull attributes which are explained later.
This INegotiator is also used in the z3c.language.switch package.

This package contains tests for Zope3 i18n language negotiator.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

