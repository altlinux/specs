%define oname z3c.authenticator

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2.a5.1
Summary: IAuthentication implementation for for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.authenticator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.configurator z3c.contents z3c.form
%py_requires z3c.formui z3c.template zope.app.generations
%py_requires zope.authentication zope.component zope.container
%py_requires zope.deprecation zope.dublincore zope.event zope.i18n
%py_requires zope.interface zope.lifecycleevent zope.location
%py_requires zope.password zope.principalregistry zope.publisher
%py_requires zope.schema zope.security zope.session zope.site
%py_requires zope.traversing

%description
This package provides an IAuthentication implementation for Zope3. Note
that this implementation is independent of zope.app.authentication and
it doesn't depend on that package. This means it doesn't even use the
credential or authentication plugins offered from
zope.app.authentication package.

%package -n python3-module-%oname
Summary: IAuthentication implementation for for Zope3
Group: Development/Python3
%py3_requires z3c.configurator z3c.contents z3c.form
%py3_requires z3c.formui z3c.template zope.app.generations
%py3_requires zope.authentication zope.component zope.container
%py3_requires zope.deprecation zope.dublincore zope.event zope.i18n
%py3_requires zope.interface zope.lifecycleevent zope.location
%py3_requires zope.password zope.principalregistry zope.publisher
%py3_requires zope.schema zope.security zope.session zope.site
%py3_requires zope.traversing

%description -n python3-module-%oname
This package provides an IAuthentication implementation for Zope3. Note
that this implementation is independent of zope.app.authentication and
it doesn't depend on that package. This means it doesn't even use the
credential or authentication plugins offered from
zope.app.authentication package.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.authenticator
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.testing zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package provides an IAuthentication implementation for Zope3. Note
that this implementation is independent of zope.app.authentication and
it doesn't depend on that package. This means it doesn't even use the
credential or authentication plugins offered from
zope.app.authentication package.

This package contains tests for z3c.authenticator.

%package tests
Summary: Tests for z3c.authenticator
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.testing zope.app.testing zope.testing

%description tests
This package provides an IAuthentication implementation for Zope3. Note
that this implementation is independent of zope.app.authentication and
it doesn't depend on that package. This means it doesn't even use the
credential or authentication plugins offered from
zope.app.authentication package.

This package contains tests for z3c.authenticator.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a5.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.a5
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a5
- Version 1.0.0a5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt3
- Removed setuptools from requirements

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus

