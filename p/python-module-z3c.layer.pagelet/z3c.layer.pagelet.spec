%define oname z3c.layer.pagelet

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a1.1
Summary: Pagelet layer setup for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.pagelet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.pagelet z3c.template zope.authentication zope.browser
%py_requires zope.browserresource zope.component zope.interface
%py_requires zope.login zope.publisher
Requires: python-module-z3c.layer

%description
This package provides a pagelet based layer setup for Zope3.

%package -n python3-module-%oname
Summary: Pagelet layer setup for Zope 3
Group: Development/Python3
%py3_requires z3c.pagelet z3c.template zope.authentication zope.browser
%py3_requires zope.browserresource zope.component zope.interface
%py3_requires zope.login zope.publisher
Requires: python3-module-z3c.layer

%description -n python3-module-%oname
This package provides a pagelet based layer setup for Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for Pagelet layer setup for Zope 3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testbrowser zope.app.wsgi zope.exceptions
%py3_requires zope.principalregistry zope.publisher zope.security
%py3_requires zope.securitypolicy zope.testing

%description -n python3-module-%oname-tests
This package provides a pagelet based layer setup for Zope3.

This package contains tests for Pagelet layer setup for Zope 3.

%package tests
Summary: Tests for Pagelet layer setup for Zope 3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.wsgi zope.exceptions
%py_requires zope.principalregistry zope.publisher zope.security
%py_requires zope.securitypolicy zope.testing

%description tests
This package provides a pagelet based layer setup for Zope3.

This package contains tests for Pagelet layer setup for Zope 3.

%package -n python-module-z3c.layer
Summary: Core package of z3c.layer
Group: Development/Python

%description -n python-module-z3c.layer
This package contains core package of z3c.layer.

%package -n python3-module-z3c.layer
Summary: Core package of z3c.layer
Group: Development/Python3

%description -n python3-module-z3c.layer
This package contains core package of z3c.layer.

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
touch %buildroot%python_sitelibdir/z3c/layer/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/layer/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/z3c/layer/__init__.py*

%files tests
%python_sitelibdir/*/*/*/test*

%files -n python-module-z3c.layer
%dir %python_sitelibdir/z3c/layer
%python_sitelibdir/z3c/layer/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/z3c/layer/__init__.py
%exclude %python3_sitelibdir/z3c/layer/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-z3c.layer
%python3_sitelibdir/z3c/layer/__init__.py
%python3_sitelibdir/z3c/layer/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

