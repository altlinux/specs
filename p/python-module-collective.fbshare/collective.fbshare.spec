%define mname collective
%define oname %mname.fbshare
Name: python-module-%oname
Version: 0.3.2
Release: alt1.dev0.git20150220
Summary: Provide some additional Open Graph meta tag in your Plone site
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.fbshare/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.fbshare.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.contentleadimage
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-sc.social.like

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.registry collective.contentleadimage
%py_requires Products.CMFCore Products.statusmessages plone.registry
%py_requires plone.memoize plone.app.layout zope.i18nmessageid z3c.form
%py_requires zope.schema zope.app.schema zope.interface zope.component
%py_requires sc.social.like

%description
Add new meta tags to you Plone site, for better controlling how your
items are shared on Facebook.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
Add new meta tags to you Plone site, for better controlling how your
items are shared on Facebook.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev0.git20150220
- Initial build for Sisyphus

