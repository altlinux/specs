%define mname eea
%define oname %mname.design

%def_disable check

Name: python-module-%oname
Version: 10.8
Release: alt1
Summary: Plone4 theme for EEA
License: GPLv2+
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.design/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.EEAPloneAdmin
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.NavigationManager
BuildPreReq: python-module-Products.eeawebapplication
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-eea.converter
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-eea.icons
BuildPreReq: python-module-eea.promotion
BuildPreReq: python-module-eea.translations
BuildPreReq: python-module-valentine.linguaflow
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plonetheme.sunburst
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-eea.themecentre

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.EEAContentTypes Products.EEAPloneAdmin
%py_requires Products.LinguaPlone Products.NavigationManager eea.cache
%py_requires Products.eeawebapplication eea.converter eea.icons
%py_requires eea.facetednavigation eea.promotion eea.translations
%py_requires valentine.linguaflow Products.CMFCore Products.CMFPlone
%py_requires Products.CMFEditions Products.statusmessages plone.memoize
%py_requires Products.PythonScripts plone.app.portlets plone.portlets
%py_requires plone.theme plonetheme.sunburst plone.app.blob zope.viewlet
%py_requires plone.app.layout plone.app.discussion zope.component
%py_requires zope.interface zope.publisher zope.app.annotation
%py_requires zope.i18nmessageid
#py_requires eea.themecentre

%description
Plone4 theme for EEA.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Plone4 theme for EEA.

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
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8-alt1
- Initial build for Sisyphus

