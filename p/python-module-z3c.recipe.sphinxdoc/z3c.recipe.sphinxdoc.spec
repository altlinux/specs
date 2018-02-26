%define oname z3c.recipe.sphinxdoc
Name: python-module-%oname
Version: 0.0.8
Release: alt4.1
Summary: Use Sphinx to build documentation for zope.org
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.sphinxdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-zc.buildout

%py_requires z3c z3c.recipe zc.buildout zc.recipe.egg docutils
%py_requires sphinx

%description
This buildout recipe aids in the generation of documentation for the
zope.org website from restructured text files located in a package. It
uses Sphinx to build static html files which can stand alone as a very
nice looking website.

%package -n python-module-z3c.recipe
Summary: Core package for z3c.repice
Group: Development/Python

%description -n python-module-z3c.recipe
This buildout recipe aids in the generation of documentation for the
zope.org website from restructured text files located in a package. It
uses Sphinx to build static html files which can stand alone as a very
nice looking website.

This package contains Core package for z3c.repice.

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
touch %buildroot%python_sitelibdir/z3c/recipe/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/z3c/recipe/__init__.py*

%files -n python-module-z3c.recipe
%python_sitelibdir/z3c/recipe/__init__.py*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.8-alt4.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt4
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt3
- Fixed requirements

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt2
- Set archdep for package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus

