%define mname eea
%define oname %mname.facetednavigation
Name: python-module-%oname
Version: 7.5
Release: alt1.dev.git20141212
Summary: Faceted Navigation for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.facetednavigation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.facetednavigation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.faceted.vocabularies
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.browsermenu

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.app.publisher zope.browsermenu
%py_requires zope.event zope.publisher zope.traversing zope.security
%py_requires zope.pagetemplate zope.browserpage zope.annotation
%py_requires zope.configuration zope.schema zope.app.pagetemplate
%py_requires zope.interface zope.annotation zope.i18nmessageid zope.i18n
%py_requires plone.app.querystring Products.LinguaPlone zope.component
%py_requires plone.app.layout plone.registry plone.app.collection
%py_requires Products.ResourceRegistries plone.app.contentmenu
%py_requires Products.CMFPlone Products.ATContentTypes plone.i18n
%py_requires Products.statusmessages Products.Archetypes plone.indexer
%py_requires %mname eea.faceted.vocabularies collective.js.jqueryui
%py_requires eea.jquery eea.cache Products.GenericSetup Products.CMFCore

%description
The EEA Faceted Navigation (FacetedNav) gives you a very powerful
interface to improve search within large collections of items. No
programming skills are required by the website manager to configure the
faceted navigation interface, configuration is done TTW. It lets you
gradually select and explore different facets (metadata/properties) of
the site content and narrow down you search quickly and dynamically.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
The EEA Faceted Navigation (FacetedNav) gives you a very powerful
interface to improve search within large collections of items. No
programming skills are required by the website manager to configure the
faceted navigation interface, configuration is done TTW. It lets you
gradually select and explore different facets (metadata/properties) of
the site content and narrow down you search quickly and dynamically.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR %mname/facetednavigation %buildroot%python_sitelibdir/%mname/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.md *.rst *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/*/tests.*
%exclude %python_sitelibdir/%mname/*/*/example

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/*/tests.*
%python_sitelibdir/%mname/*/*/example

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.5-alt1.dev.git20141212
- Initial build for Sisyphus

