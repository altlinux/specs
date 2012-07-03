%define oname z3c.authenticator
Name: python-module-%oname
Version: 0.8.1
Release: alt3.1
Summary: IAuthentication implementation for for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.authenticator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt3
- Removed setuptools from requirements

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus

