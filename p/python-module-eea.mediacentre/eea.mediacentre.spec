%define mname eea
%define oname %mname.mediacentre

%def_disable check

Name: python-module-%oname
Version: 6.3
Release: alt1
Summary: EEA Media Centre
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.mediacentre/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-eea.geotags
BuildPreReq: python-module-Products.EEAContentTypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-valentine.linguaflow
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.EEAPloneAdmin
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-eea.themecentre
#BuildPreReq: python-module-eea.dataservice
#BuildPreReq: python-module-eea.design

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.vocab eea.geotags Products.EEAContentTypes
%py_requires Products.LinguaPlone valentine.linguaflow eea.forms
%py_requires Products.ATVocabularyManager Products.EEAPloneAdmin
%py_requires Products.Archetypes Products.CMFCore Products.CMFPlone
%py_requires Products.ATContentTypes plone.app.blob zope.component
%py_requires zope.interface zope.schema zope.annotation zope.formlib
%py_requires zope.i18nmessageid
#py_requires eea.themecentre eea.dataservice eea.design

%description
Media Centre offers an API to search for media content on the website.
The actual content is looked up by plugins. A plugin should register
itself as a utility that provides IMediaCentrePlugin. Then media centre
will find it and can ask it what media content it provides.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Media Centre offers an API to search for media content on the website.
The actual content is looked up by plugins. A plugin should register
itself as a utility that provides IMediaCentrePlugin. Then media centre
will find it and can ask it what media content it provides.

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
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3-alt1
- Initial build for Sisyphus

