%define oname z3c.recipe.i18n
Name: python-module-%oname
Version: 0.8.0
Release: alt2.1
Summary: Zope3 egg based i18n locales extration recipes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.buildout z3c.recipe.scripts zope.app.appsetup
%py_requires zope.app.locales zope.configuration

%description
This Zope 3 recipes offers different tools which allows to extract i18n
translation messages from egg based packages.

%package tests
Summary: Tests for z3c.recipe.i18n
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zc.lockfile zope.app.publication
%py_requires zope.component zope.configuration zope.container zope.error
%py_requires zope.event zope.interface zope.location
%py_requires zope.processlifetime zope.session zope.site zope.security
%py_requires zope.traversing ZODB3

%description tests
This Zope 3 recipes offers different tools which allows to extract i18n
translation messages from egg based packages.

This package contains tests for z3c.recipe.i18n.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

