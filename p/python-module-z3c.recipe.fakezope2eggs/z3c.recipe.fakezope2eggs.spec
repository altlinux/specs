%define oname z3c.recipe.fakezope2eggs

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt4.1
Summary: ZC Buildout recipe to fake zope 2 packages as eggs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.fakezope2eggs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.recipe zc.buildout

%description
Zope 2 isn't eggified yet, Zope 3 does. That can become a problem if you
want to install some egg with depedencies related to Zope 3 eggs (such
as zope.interface, zope.component, ...)

This buildout recipe will simply add some fake egg link to zope
libraries (installed inside zope/lib/python/zope/...) so that setuptools
can see that the dependencies are already satisfied and it won't fetch
them anymore.

%package -n python3-module-%oname
Summary: ZC Buildout recipe to fake zope 2 packages as eggs
Group: Development/Python3
%py3_requires z3c.recipe zc.buildout

%description -n python3-module-%oname
Zope 2 isn't eggified yet, Zope 3 does. That can become a problem if you
want to install some egg with depedencies related to Zope 3 eggs (such
as zope.interface, zope.component, ...)

This buildout recipe will simply add some fake egg link to zope
libraries (installed inside zope/lib/python/zope/...) so that setuptools
can see that the dependencies are already satisfied and it won't fetch
them anymore.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.recipe.fakezope2eggs
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Zope 2 isn't eggified yet, Zope 3 does. That can become a problem if you
want to install some egg with depedencies related to Zope 3 eggs (such
as zope.interface, zope.component, ...)

This buildout recipe will simply add some fake egg link to zope
libraries (installed inside zope/lib/python/zope/...) so that setuptools
can see that the dependencies are already satisfied and it won't fetch
them anymore.

This package contains tests for z3c.recipe.fakezope2eggs.

%package tests
Summary: Tests for z3c.recipe.fakezope2eggs
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Zope 2 isn't eggified yet, Zope 3 does. That can become a problem if you
want to install some egg with depedencies related to Zope 3 eggs (such
as zope.interface, zope.component, ...)

This buildout recipe will simply add some fake egg link to zope
libraries (installed inside zope/lib/python/zope/...) so that setuptools
can see that the dependencies are already satisfied and it won't fetch
them anymore.

This package contains tests for z3c.recipe.fakezope2eggs.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Fixed requirements

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

