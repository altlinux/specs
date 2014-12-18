%define mname eea
%define oname %mname.indicators

%def_disable check

Name: python-module-%oname
Version: 9.2
Release: alt1
Summary: EEA Indicators
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.indicators/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-Products.UserAndGroupSelectionWidget
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-eea.themecentre
BuildPreReq: python-module-eea.workflow
BuildPreReq: python-module-eea.relations
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-eea.tags
BuildPreReq: python-module-eea.app.visualization
BuildPreReq: python-module-Products.CompoundField
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-eea.depiction
BuildPreReq: python-module-eea.rdfmarshaller
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-eea.dataservice

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ATVocabularyManager Products.DataGridField
%py_requires Products.UserAndGroupSelectionWidget eea.facetednavigation
%py_requires Products.EEAContentTypes eea.themecentre eea.workflow
%py_requires eea.relations zope.traversing eea.forms eea.tags plone.uuid
%py_requires eea.app.visualization Products.CompoundField eea.versions
%py_requires eea.depiction eea.rdfmarshaller Products.CMFCore zope.event
%py_requires Products.statusmessages Products.CMFPlone plone.app.layout
%py_requires Products.EEAContentTypes Products.CMFDynamicViewFTI
%py_requires Products.Archetypes Products.ATContentTypes plone.app.blob
%py_requires Products.validation plone.app.portlets zope.publisher
%py_requires zope.interface zope.component zope.lifecycleevent
%py_requires zope.schema zope.annotation zope.i18nmessageid
#py_requires eea.dataservice

%description
EEA Indicators.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
EEA Indicators.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.2-alt1
- Initial build for Sisyphus

