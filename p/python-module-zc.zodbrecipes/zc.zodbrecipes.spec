%define oname zc.zodbrecipes
Name: python-module-%oname
Version: 0.6.1
Release: alt3.1
Summary: ZC Buildout recipes for ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zodbrecipes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description
Recipes for working with ZODB.

%package tests
Summary: Tests for zc.zodbrecipes
Group: Development/Python
Requires: %name = %version-%release
%py_requires zdaemon ZODB3

%description tests
Recipes for working with ZODB.

This package contains tests for zc.zodbrecipes.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Removed setuptools from requirements

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

