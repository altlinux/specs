%define oname z3c.recipe.dev

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt4.1
Summary: Zope3 development server setup recipes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.dev/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.recipe ZConfig zc.buildout zc.recipe.egg zope.testing

%description
The z3c.recipe.dev:app generates start scripts and configuration files
for starting a egg based Zope 3 setup.

The z3c.recipe.dev:script generates a hook to a existing python module
and allows to execute a python method including eggs in sys path.

%package -n python3-module-%oname
Summary: Zope3 development server setup recipes
Group: Development/Python3
%py3_requires z3c.recipe ZConfig zc.buildout zc.recipe.egg zope.testing

%description -n python3-module-%oname
The z3c.recipe.dev:app generates start scripts and configuration files
for starting a egg based Zope 3 setup.

The z3c.recipe.dev:script generates a hook to a existing python module
and allows to execute a python method including eggs in sys path.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 development server setup recipe
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.recipe.filestorage

%description -n python3-module-%oname-tests
The z3c.recipe.dev:app generates start scripts and configuration files
for starting a egg based Zope 3 setup.

The z3c.recipe.dev:script generates a hook to a existing python module
and allows to execute a python method including eggs in sys path.

This package contains tests for Zope3 development server setup recipe.

%package tests
Summary: Tests for Zope3 development server setup recipe
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.recipe.filestorage

%description tests
The z3c.recipe.dev:app generates start scripts and configuration files
for starting a egg based Zope 3 setup.

The z3c.recipe.dev:script generates a hook to a existing python module
and allows to execute a python method including eggs in sys path.

This package contains tests for Zope3 development server setup recipe.

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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Fixed requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

