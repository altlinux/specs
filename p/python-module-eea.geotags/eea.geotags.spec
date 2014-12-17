%define mname eea
%define oname %mname.geotags
Name: python-module-%oname
Version: 6.8
Release: alt1
Summary: Easy define locations using a map picker and http://geonames.org geographical database
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.geotags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-eea.alchemy
BuildPreReq: python-module-eea.rdfmarshaller
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ATVocabularyManager eea.jquery eea.alchemy
%py_requires archetypes.schemaextender eea.rdfmarshaller eea.cache
%py_requires Products.CMFCore Products.Archetypes plone.indexer
%py_requires Products.ATContentTypes zope.interface zope.schema
%py_requires zope.component zope.browserpage zope.app.form zope.i18n
%py_requires zope.annotation zope.i18nmessageid

%description
EEA Geotags package redefines the location field in Plone. Right now in
Plone location field is a free text field. EEA Geotags lets you easy
define locations using a map picker and http://geonames.org geographical
database.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
EEA Geotags package redefines the location field in Plone. Right now in
Plone location field is a free text field. EEA Geotags lets you easy
define locations using a map picker and http://geonames.org geographical
database.

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
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.8-alt1
- Initial build for Sisyphus

