%define oname zc.zodbrecipes

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.1
Summary: ZC Buildout recipes for ZODB
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zodbrecipes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description
Recipes for working with ZODB.

%package -n python3-module-%oname
Summary: ZC Buildout recipes for ZODB
Group: Development/Python3
%py3_requires zc zc.buildout zope.testing zc.recipe.egg ZConfig

%description -n python3-module-%oname
Recipes for working with ZODB.

%package -n python3-module-%oname-tests
Summary: Tests for zc.zodbrecipes
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zdaemon ZODB3

%description -n python3-module-%oname-tests
Recipes for working with ZODB.

This package contains tests for zc.zodbrecipes.

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

%if_with python3
cp -fR . ../python3
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Removed setuptools from requirements

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

