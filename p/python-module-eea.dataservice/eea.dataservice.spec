%define mname eea
%define oname %mname.dataservice
Name: python-module-%oname
Version: 8.6
Release: alt1
Summary: EEA Data service
License: GPLv2+
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.dataservice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow python-module-rarfile
BuildPreReq: python-module-mock python-module-uuid
BuildPreReq: python-module-openid
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-eea.workflow
BuildPreReq: python-module-eea.geotags
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-plone.app.async
BuildPreReq: python-module-eea.indicators
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zc.twist
BuildPreReq: python-module-Products.EEAPloneAdmin
BuildPreReq: python-module-eea.soer
BuildPreReq: python-module-eea.reports

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname PIL Products.ATVocabularyManager eea.cache eea.forms
%py_requires Products.CMFPlacefulWorkflow eea.jquery eea.versions
%py_requires eea.vocab eea.workflow eea.geotags five.intid plone.memoize
%py_requires plone.app.async eea.indicators collective.quickupload
%py_requires Products.statusmessages Products.CMFPlone Products.CMFCore
%py_requires Products.Archetypes Products.EEAContentTypes plone.i18n
%py_requires Products.ATContentTypes Products.validation plone.app.blob
%py_requires Products.PythonScripts Products.MimetypesRegistry zc.twist
%py_requires plone.indexer zope.component zope.interface zope.publisher
%py_requires zope.browserpage zope.schema zope.annotation eea.reports

%description
EEA Data service.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.EEAPloneAdmin

%description tests
EEA Data service.

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
%exclude %python_sitelibdir/%mname/*/*/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/*/tests.*

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.6-alt1
- Initial build for Sisyphus

