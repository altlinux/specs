%define oname z3c.recipe.i18n

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt2.1
Summary: Zope3 egg based i18n locales extration recipes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.buildout z3c.recipe.scripts zope.app.appsetup
%py_requires zope.app.locales zope.configuration z3c.recipe

%description
This Zope 3 recipes offers different tools which allows to extract i18n
translation messages from egg based packages.

%package -n python3-module-%oname
Summary: Zope3 egg based i18n locales extration recipes
Group: Development/Python3
%py3_requires zc.buildout z3c.recipe.scripts zope.app.appsetup
%py3_requires zope.app.locales zope.configuration z3c.recipe

%description -n python3-module-%oname
This Zope 3 recipes offers different tools which allows to extract i18n
translation messages from egg based packages.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.recipe.i18n
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zc.lockfile zope.app.publication
%py3_requires zope.component zope.configuration zope.container zope.error
%py3_requires zope.event zope.interface zope.location
%py3_requires zope.processlifetime zope.session zope.site zope.security
%py3_requires zope.traversing ZODB3

%description -n python3-module-%oname-tests
This Zope 3 recipes offers different tools which allows to extract i18n
translation messages from egg based packages.

This package contains tests for z3c.recipe.i18n.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

