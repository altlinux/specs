%define oname zc.zope3recipes

%def_with python3

Name: python-module-%oname
Version: 0.18.0
Release: alt2.1
Summary: ZC Buildout recipe for defining Zope 3 applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zope3recipes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description
Recipes for creating Zope 3 instances with distinguishing features:

  * Don't use a skeleton
  * Separates application and instance definition
  * Don't support package-includes

Unfortunately, partial Windows support at this time. It works but it's
alpha.

%package -n python3-module-%oname
Summary: ZC Buildout recipe for defining Zope 3 applications
Group: Development/Python3
%py3_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description -n python3-module-%oname
Recipes for creating Zope 3 instances with distinguishing features:

  * Don't use a skeleton
  * Separates application and instance definition
  * Don't support package-includes

Unfortunately, partial Windows support at this time. It works but it's
alpha.

%package -n python3-module-%oname-tests
Summary: Tests for zc.zope3recipes
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zdaemon zc.recipe.filestorage

%description -n python3-module-%oname-tests
Recipes for creating Zope 3 instances with distinguishing features:

  * Don't use a skeleton
  * Separates application and instance definition
  * Don't support package-includes

Unfortunately, partial Windows support at this time. It works but it's
alpha.

This package contains tests for zc.zope3recipes.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.18.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.0-alt1
- Version 0.18.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus

