%define oname z3c.recipe.runscript
Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: A recipe that runs any script to install a part
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.runscript/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout

%description
This run-script URL allows you to specify an arbitrary script to do the
work of the recipe.

%package tests
Summary: Tests for z3c.recipe.runscript
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This run-script URL allows you to specify an arbitrary script to do the
work of the recipe.

This package contains tests for z3c.recipe.runscript.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Version 0.1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

