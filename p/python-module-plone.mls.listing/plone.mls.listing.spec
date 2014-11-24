%define mname plone.mls
%define oname %mname.listing
Name: python-module-%oname
Version: 1.0
Release: alt1.dev.git20141124
Summary: Plone support for MLS Listings
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.mls.listing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/propertyshelf/plone.mls.listing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Pillow
BuildPreReq: python-module-Zope2-tests python-module-openid
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-collective.prettyphoto
BuildPreReq: python-module-mls.apiclient
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.app.versioningbehavior
BuildPreReq: python-module-plone.formwidget.captcha
BuildPreReq: python-module-ps.plone.fotorama
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.contentleadimage
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.mls.core
BuildPreReq: python-module-raptus.article.core

%py_provides %oname
Requires: python-module-Zope2
%py_requires collective.autopermission collective.prettyphoto plone.api
%py_requires mls.apiclient plone.app.dexterity plone.app.relationfield
%py_requires plone.app.referenceablebehavior plone.formwidget.captcha
%py_requires plone.app.versioningbehavior plone.mls.core zope.interface
%py_requires ps.plone.fotorama collective.contentleadimage zope.schema
%py_requires Products.CMFCore Products.CMFPlone Products.CMFEditions
%py_requires zope.component zope.traversing zope.annotation zope.i18n
%py_requires zope.publisher zope.formlib zope.i18nmessageid z3c.form
%py_requires zope.globalrequest raptus.article.core

%description
Plone support for MLS Listings.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
Plone support for MLS Listings.

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
%python_sitelibdir/plone/mls/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/mls/*/test*

%files tests
%python_sitelibdir/plone/mls/*/test*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.dev.git20141124
- Initial build for Sisyphus

