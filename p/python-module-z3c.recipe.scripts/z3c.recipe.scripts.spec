%define oname z3c.recipe.scripts
Name: python-module-%oname
Version: 1.0.1
Release: alt1.1
Summary: Recipe for installing Python scripts
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.scripts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout zc.recipe.egg

%description
The script recipe installs eggs into a buildout eggs directory, exactly
like zc.recipe.egg, and then generates scripts in a buildout bin
directory with egg paths baked into them.

%package tests
Summary: Tests for z3c.recipe.scripts
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The script recipe installs eggs into a buildout eggs directory, exactly
like zc.recipe.egg, and then generates scripts in a buildout bin
directory with egg paths baked into them.

This package contains tests for z3c.recipe.scripts.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

