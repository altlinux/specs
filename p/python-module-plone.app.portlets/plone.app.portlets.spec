%define oname plone.app.portlets

Name: python-module-%oname
Version: 3.0.2
Release: alt2.dev0.git20141009
Summary: Plone integration for the basic plone.portlets package
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.portlets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.portlets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction python-module-feedparser
BuildPreReq: python-module-five.customerize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.i18n
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.GenericSetup Products.PluggableAuthService
%py_requires Products.CMFCore Products.CMFDynamicViewFTI ZODB3
%py_requires zope.publisher zope.schema zope.site zope.traversing
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.configuration zope.contentprovider zope.event
%py_requires zope.annotation zope.browser zope.component zope.container
%py_requires plone.portlets plone.app.i18n plone.app.vocabularies
%py_requires plone.app five.customerize plone.i18n plone.memoize
%py_requires plone.app.layout Products.CMFPlone

%description
plone.app.portlets provides a Plone-specific user interface for
plone.portlets, as well as a standard set of portlets that ship with
Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.blob plone.app.testing
%py_requires Products.ATContentTypes

%description tests
plone.app.portlets provides a Plone-specific user interface for
plone.portlets, as well as a standard set of portlets that ship with
Plone.

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
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.dev0.git20141009
- Initial build for Sisyphus

