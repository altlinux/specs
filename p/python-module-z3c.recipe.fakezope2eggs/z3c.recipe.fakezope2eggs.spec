%define oname z3c.recipe.fakezope2eggs
Name: python-module-%oname
Version: 0.5
Release: alt3.1
Summary: ZC Buildout recipe to fake zope 2 packages as eggs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.fakezope2eggs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout

%description
Zope 2 isn't eggified yet, Zope 3 does. That can become a problem if you
want to install some egg with depedencies related to Zope 3 eggs (such
as zope.interface, zope.component, ...)

This buildout recipe will simply add some fake egg link to zope
libraries (installed inside zope/lib/python/zope/...) so that setuptools
can see that the dependencies are already satisfied and it won't fetch
them anymore.

%package tests
Summary: Tests for z3c.recipe.fakezope2eggs
Group: Development/Python
Requires: %name = %version-%release

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Fixed requirements

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

