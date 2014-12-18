%define mname eea
%define oname %mname.themecentre

%def_disable check

Name: python-module-%oname
Version: 6.2
Release: alt1
Summary: EEA Theme centre
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.themecentre/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.FiveSite
BuildPreReq: python-module-Products.PloneHelpCenter
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.EEAPloneAdmin
BuildPreReq: python-module-valentine.linguaflow
BuildPreReq: python-module-eea.design
BuildPreReq: python-module-eea.promotion
BuildPreReq: python-module-eea.mediacentre
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.NavigationManager
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-eea.soer
#BuildPreReq: python-module-eea.indicators

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.FiveSite Products.PloneHelpCenter
%py_requires Products.ATVocabularyManager Products.LinguaPlone
%py_requires Products.EEAPloneAdmin valentine.linguaflow eea.design
%py_requires eea.promotion eea.mediacentre eea.vocab eea.versions
%py_requires Products.EEAContentTypes Products.CMFPlone Products.CMFCore
%py_requires Products.NavigationManager Products.ATContentTypes
%py_requires Products.validation Products.ZCatalog plone.app.portlets
%py_requires plone.portlets plone.app.layout plone.indexer zope.event
%py_requires zope.lifecycleevent zope.annotation zope.interface
%py_requires zope.component zope.formlib zope.schema zope.publisher
%py_requires zope.app.form zope.i18nmessageid plone.app.form
#py_requires eea.indicators

%description
Theme Centre is a folder that contains content on a certain theme.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing zope.site

%description tests
Theme Centre is a folder that contains content on a certain theme.

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
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2-alt1
- Initial build for Sisyphus

