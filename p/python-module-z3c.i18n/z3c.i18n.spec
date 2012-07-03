%define oname z3c.i18n
Name: python-module-%oname
Version: 0.1.2
Release: alt2.1
Summary: Extensions to Zope's I18n Support
License: ZPLv2.1
Group: Development/Python
Url: http://cheeseshop.python.org/pypi/z3c.i18n
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
This package contains various i18n related convinience modules.

%package tests
Summary: Tests for Extensions to Zope's I18n Support
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains various i18n related convinience modules.

This package contains tests for Extensions to Zope's I18n Support.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

