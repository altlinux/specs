%define oname plone.app.openid

Name: python-module-%oname
Version: 2.0.3
Release: alt2.dev.git20140823
Summary: Plone OpenID authentication support
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.openid.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.openid
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-openid

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.openid plone.portlets zope.component
%py_requires zope.i18nmessageid zope.interface Products.CMFCore
%py_requires Products.PlonePAS Products.PluggableAuthService
%py_requires plone.app.portlets

%description
This package makes Plone a complete OpenID consumer, allowing people to
authenticate in a site using their OpenID identity. It relies on the
plone.openid package to implement authentication of identities and needs
an external session management plugin such as plone.session to add
session management.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package makes Plone a complete OpenID consumer, allowing people to
authenticate in a site using their OpenID identity. It relies on the
plone.openid package to implement authentication of identities and needs
an external session management plugin such as plone.session to add
session management.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2.dev.git20140823
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.dev.git20140823
- Initial build for Sisyphus

