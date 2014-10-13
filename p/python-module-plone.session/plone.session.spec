%define oname plone.session
Name: python-module-%oname
Version: 3.5.4
Release: alt1.dev0.git20140826
Summary: Session based authentication for Zope
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.session.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone plone.keyring plone.protect zope.component
%py_requires zope.interface Products.PluggableAuthService

%description
Provides secure session management for Zope sites using by default an
HMAC SHA-256 secure cryptographic hash to authenticate sessions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.configuration zope.publisher

%description tests
Provides secure session management for Zope sites using by default an
HMAC SHA-256 secure cryptographic hash to authenticate sessions.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.4-alt1.dev0.git20140826
- Initial build for Sisyphus

