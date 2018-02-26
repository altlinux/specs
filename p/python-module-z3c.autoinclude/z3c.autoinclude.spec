%define oname z3c.autoinclude
Name: python-module-%oname
Version: 0.3.4
Release: alt2.1
Summary: Automatically include ZCML
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.autoinclude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.dottedname zope.interface zope.configuration
%py_requires zope.schema zc.buildout

%description
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

%package tests
Summary: Tests for z3c.autoinclude
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

This package contains tests for z3c.autoinclude.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%_bindir/*
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

