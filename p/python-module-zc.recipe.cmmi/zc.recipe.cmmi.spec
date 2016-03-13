%define oname zc.recipe.cmmi

%def_with python3

Name: python-module-%oname
Version: 1.3.6
Release: alt1.1
Summary: ZC Buildout recipe for configure/make/make install
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.cmmi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.recipe zc.buildout

%description
The configure-make-make-install recipe automates installation of
configure-based source distribution into buildouts.

%package -n python3-module-%oname
Summary: ZC Buildout recipe for configure/make/make install
Group: Development/Python3
%py3_requires zc.recipe zc.buildout

%description -n python3-module-%oname
The configure-make-make-install recipe automates installation of
configure-based source distribution into buildouts.

%package -n python3-module-%oname-tests
Summary: Tests for zc.recipe.cmmi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The configure-make-make-install recipe automates installation of
configure-based source distribution into buildouts.

This package contains tests for zc.recipe.cmmi.

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

%package -n python3-module-zc.recipe
Summary: Core package of zc.recipe
Group: Development/Python3
%py3_provides zc.recipe

%description -n python3-module-zc.recipe
Core package of zc.recipe.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
touch %buildroot%python_sitelibdir/zc/recipe/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/zc/recipe/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zc/recipe/__init__.py
%exclude %python3_sitelibdir/zc/recipe/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-zc.recipe
%python3_sitelibdir/zc/recipe/__init__.py
%python3_sitelibdir/zc/recipe/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1
- Version 1.3.6
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1
- Version 1.3.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Initial build for Sisyphus

