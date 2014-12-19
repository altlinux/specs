%define oname Products.EEAContentTypes

Name: python-module-%oname
Version: 9.7
Release: alt2
Summary: EEA logic and content types
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/products.eeacontenttypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-uuid python-module-mock
BuildPreReq: python-module-openid python-module-windmill
BuildPreReq: python-module-Products.LinguaPlone python-module-rdflib
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.OrderableReferenceField
BuildPreReq: python-module-Products.RedirectionTool
BuildPreReq: python-module-Products.EEAPloneAdmin
BuildPreReq: python-module-Products.NavigationManager
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-valentine.linguaflow
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.PlacelessTranslationService
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-collective.deletepermission
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-surf
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-eea.mediacentre
BuildPreReq: python-module-eea.themecentre
BuildPreReq: python-module-eea.rdfmarshaller
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-eea.translations
BuildPreReq: python-module-eea.promotion
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-eea.depiction
BuildPreReq: python-module-eea.reports
BuildPreReq: python-module-eea.relations
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-eea.dataservice
BuildPreReq: python-module-eea.design
BuildPreReq: python-module-eea.geotags
BuildPreReq: python-module-eea.indicators
BuildPreReq: python-module-eea.soer

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.browserpage zope.i18nmessageid z3c.caching
%py_requires zope.lifecycleevent zope.annotation zope.formlib
%py_requires zope.interface zope.component zope.event zope.publisher
%py_requires plone.indexer plone.registry plone.app.viewletmanager
%py_requires plone.keyring plone.contentrules plone.app.contentrules
%py_requires plone.app.imaging plone.app.blob plone.protect zope.schema
%py_requires Products.PlacelessTranslationService plone.app.caching
%py_requires Products.PythonScripts Products.PortalTransforms plone.i18n
%py_requires Products.validation Products.CMFEditions plone.app.layout
%py_requires Products.CMFCore Products.CMFPlone Products.ATContentTypes
%py_requires Products.Archetypes Products.statusmessages plone.memoize
%py_requires Products.LinguaPlone Products.ATVocabularyManager
%py_requires Products.OrderableReferenceField Products.RedirectionTool
%py_requires Products.EEAPloneAdmin Products.NavigationManager
%py_requires collective.monkeypatcher
%py_requires eea.rdfmarshaller eea.facetednavigation eea.forms eea.vocab
%py_requires eea.mediacentre eea.themecentre eea.translations eea.cache
%py_requires eea.promotion eea.depiction eea.reports eea.relations

%description
EEA logic and content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires valentine.linguaflow collective.deletepermission
%py_requires Products.PloneTestCase Products.MailHost
%py_requires eea.dataservice eea.design eea.geotags eea.indicators
%py_requires eea.soer

%description tests
EEA logic and content types.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/*/test*
%exclude %python_sitelibdir/Products/*/*tests*

%files tests
%python_sitelibdir/Products/*/*/test*
%python_sitelibdir/Products/*/*tests*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.7-alt2
- Added necessary requirements
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.7-alt1
- Initial build for Sisyphus

