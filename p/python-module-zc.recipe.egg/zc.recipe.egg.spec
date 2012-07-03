%define oname zc.recipe.egg
Name: python-module-%oname
Version: 1.3.2
Release: alt2.1
Summary: Recipe for installing Python package distributions as eggs
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.egg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.recipe zc.buildout

%description
The egg-installation recipe installs eggs into a buildout eggs
directory. It also generates scripts in a buildout bin directory with
egg paths baked into them.

%package tests
Summary: Tests for zc.recipe.egg
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The egg-installation recipe installs eggs into a buildout eggs
directory. It also generates scripts in a buildout bin directory with
egg paths baked into them.

This package contains tests for zc.recipe.egg.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus

