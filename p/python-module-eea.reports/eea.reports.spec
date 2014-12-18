%define mname eea
%define oname %mname.reports
Name: python-module-%oname
Version: 6.0
Release: alt1
Summary: EEA Reports
License: GPLv2+
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.reports/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.AddRemoveWidget
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-eea.vocab
BuildPreReq: python-module-eea.depiction
BuildPreReq: python-module-eea.relations
BuildPreReq: python-module-eea.rdfmarshaller
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.blob-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ATVocabularyManager Products.LinguaPlone
%py_requires Products.AddRemoveWidget eea.forms eea.vocab eea.depiction
%py_requires eea.relations eea.rdfmarshaller Products.validation
%py_requires Products.CMFPlone Products.Archetypes Products.CMFCore
%py_requires Products.statusmessages plone.app.blob zope.interface
%py_requires zope.component zope.publisher zope.schema zope.event

%description
The EEA Reports Product can be used to organise printed publications
that are available online for download. Such Reports usually have a
publication date, order and ISBN numbers, an author and exist in several
language versions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase plone.app.blob.tests

%description tests
The EEA Reports Product can be used to organise printed publications
that are available online for download. Such Reports usually have a
publication date, order and ISBN numbers, an author and exist in several
language versions.

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
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0-alt1
- Initial build for Sisyphus

