%define oname zc.zope3recipes
Name: python-module-%oname
Version: 0.15.0
Release: alt1
Summary: ZC Buildout recipe for defining Zope 3 applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zope3recipes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description
Recipes for creating Zope 3 instances with distinguishing features:

  * Don't use a skeleton
  * Separates application and instance definition
  * Don't support package-includes

Unfortunately, partial Windows support at this time. It works but it's
alpha.

%package tests
Summary: Tests for zc.zope3recipes
Group: Development/Python
Requires: %name = %version-%release
%py_requires zdaemon zc.recipe.filestorage

%description tests
Recipes for creating Zope 3 instances with distinguishing features:

  * Don't use a skeleton
  * Separates application and instance definition
  * Don't support package-includes

Unfortunately, partial Windows support at this time. It works but it's
alpha.

This package contains tests for zc.zope3recipes.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus

