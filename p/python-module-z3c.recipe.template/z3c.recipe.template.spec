%define oname z3c.recipe.template
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Buildout recipe to generate a text file from a template
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.template/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe zc.buildout

%description
This recipe can be used to generate textfiles from a (text) template.
Different to collective.recipe.template you can also specify a path to
the output file and the path will be created, if it does not exist.

%package tests
Summary: Tests for z3c.recipe.template
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This recipe can be used to generate textfiles from a (text) template.
Different to collective.recipe.template you can also specify a path to
the output file and the path will be created, if it does not exist.

This package contains tests for z3c.recipe.template.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

