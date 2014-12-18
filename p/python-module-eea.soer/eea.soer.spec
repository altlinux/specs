%define mname eea
%define oname %mname.soer

Name: python-module-%oname
Version: 6.1
Release: alt2
Summary: Provides the SOER report content types
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.soer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-surf
BuildPreReq: python-module-rdflib python-module-BeautifulSoup4
BuildPreReq: python-module-uuid python-module-mock
BuildPreReq: python-module-openid
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-eea.rdfmarshaller
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-eea.faceted.inheritance
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-eea.themecentre

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.vocab eea.rdfmarshaller eea.facetednavigation
%py_requires eea.faceted.inheritance Products.ATVocabularyManager
%py_requires Products.LinguaPlone Products.PortalTransforms plone.i18n
%py_requires Products.CMFCore Products.CMFPlone Products.Marshall
%py_requires Products.Archetypes Products.ATContentTypes zope.interface
%py_requires zope.schema zope.lifecycleevent zope.event zope.component
%py_requires eea.themecentre

%description
The eea.soer package provides the SOER report content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
The eea.soer package provides the SOER report content types.

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
%exclude %python_sitelibdir/%mname/*/*/*/test*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/*/test*

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt2
- Added necessary requirements
- Enabled testing

* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt1
- Initial build for Sisyphus

