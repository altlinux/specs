%define oname z3c.recipe.sphinxdoc

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2.1
Summary: Use Sphinx to build documentation for zope.org
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.sphinxdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zc.buildout
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zc.buildout
%endif

%py_requires z3c zc.buildout zc.recipe.egg docutils
%py_requires sphinx
Requires: python-module-z3c.recipe = %EVR

%description
This buildout recipe aids in the generation of documentation for the
zope.org website from restructured text files located in a package. It
uses Sphinx to build static html files which can stand alone as a very
nice looking website.

%package -n python3-module-%oname
Summary: Use Sphinx to build documentation for zope.org
Group: Development/Python3
%py3_requires z3c zc.buildout zc.recipe.egg docutils
%py3_requires sphinx
Requires: python3-module-z3c.recipe = %EVR

%description -n python3-module-%oname
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

%package -n python3-module-z3c.recipe
Summary: Core package for z3c.repice
Group: Development/Python3

%description -n python3-module-z3c.recipe
This buildout recipe aids in the generation of documentation for the
zope.org website from restructured text files located in a package. It
uses Sphinx to build static html files which can stand alone as a very
nice looking website.

This package contains Core package for z3c.repice.

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
touch %buildroot%python_sitelibdir/z3c/recipe/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/recipe/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/z3c/recipe/__init__.py*

%files -n python-module-z3c.recipe
%python_sitelibdir/z3c/recipe/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/z3c/recipe/__init__.py
%exclude %python3_sitelibdir/z3c/recipe/__pycache__/__init__.*

%files -n python3-module-z3c.recipe
%python3_sitelibdir/z3c/recipe/__init__.py
%python3_sitelibdir/z3c/recipe/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

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

