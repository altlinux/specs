%define oname zc.recipe.cmmi
Name: python-module-%oname
Version: 1.3.5
Release: alt1
Summary: ZC Buildout recipe for configure/make/make install
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.cmmi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.recipe zc.buildout

%description
The configure-make-make-install recipe automates installation of
configure-based source distribution into buildouts.

%package tests
Summary: Tests for zc.recipe.cmmi
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The configure-make-make-install recipe automates installation of
configure-based source distribution into buildouts.

This package contains tests for zc.recipe.cmmi.

%package -n python-module-zc.recipe
Summary: Core package of zc.recipe
Group: Development/Python
%py_provides zc.recipe

%description -n python-module-zc.recipe
Core package of zc.recipe.

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

touch %buildroot%python_sitelibdir/zc/recipe/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zc/recipe/__init__.py*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-zc.recipe
%python_sitelibdir/zc/recipe/__init__.py*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1
- Version 1.3.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Initial build for Sisyphus

