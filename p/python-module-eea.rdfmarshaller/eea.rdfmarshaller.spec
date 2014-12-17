%define mname eea
%define oname %mname.rdfmarshaller
Name: python-module-%oname
Version: 7.4
Release: alt1
Summary: RDF marshaller for Plone
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.rdfmarshaller/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-uuid python-module-chardet
BuildPreReq: python-module-surf-plugins python-module-mock
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-plone.app.async
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname uuid surf_rdflib Products.ATVocabularyManager
%py_requires plone.app.async eea.versions Products.Marshall zope.event
%py_requires Products.CMFCore Products.ATContentTypes Products.CMFPlone
%py_requires Products.Archetypes Products.LinguaPlone plone.contentrules
%py_requires plone.app.contentrules plone.app.discussion zope.component
%py_requires zope.interface zope.container zope.lifecycleevent
%py_requires zope.formlib zope.schema

%description
RDF marshaller for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
RDF marshaller for Plone.

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
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.4-alt1
- Initial build for Sisyphus

