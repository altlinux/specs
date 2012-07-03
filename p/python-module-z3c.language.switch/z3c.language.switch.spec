%define oname z3c.language.switch
Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: Zope3 i18n language switch
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.language.switch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.generations zope.component zope.event zope.i18n
%py_requires zope.interface zope.lifecycleevent zope.publisher
%py_requires zope.schema zope.security

%description
This package provides an implementation wich let's you implement your
own i18n aware content types.

%package tests
Summary: Tests for Zope3 i18n language switch
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.testing zope.testing

%description tests
This package provides an implementation wich let's you implement your
own i18n aware content types.

This package contains tests for Zope3 i18n language switch.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

