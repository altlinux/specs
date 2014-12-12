%define mname collective
%define oname %mname.pwexpiry
Name: python-module-%oname
Version: 0.6
Release: alt1.dev0.git20141128
Summary: Emulate Active Directory password complexity requirements in Plone
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.pwexpiry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.pwexpiry.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openid
BuildPreReq: python-module-plone.api python-module-Plone
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.api Products.CMFPlone Products.CMFCore
%py_requires Products.PluggableAuthService Products.statusmessages
%py_requires Products.PlonePAS plone.registry plone.protect zope.event
%py_requires plone.app.controlpanel plone.app.users zope.interface
%py_requires zope.component zope.app.form zope.publisher zope.i18n
%py_requires zope.schema zope.i18nmessageid

%description
The collective.pwexpiry package is an add-on Product for Plone that
brings the feature of controlling the password expiration in Plone. It
is useful when there's a need of forcing the portal's members to follow
the specific password policy.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Plone plone.app.testing

%description tests
The collective.pwexpiry package is an add-on Product for Plone that
brings the feature of controlling the password expiration in Plone. It
is useful when there's a need of forcing the portal's members to follow
the specific password policy.

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
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev0.git20141128
- Initial build for Sisyphus

