%define mname collective
%define oname %mname.solr
Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20150219
Summary: Solr integration for external indexing and searching
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.solr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.solr.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-DateTime python-module-Plone
BuildPreReq: python-module-transaction python-module-unidecode
BuildPreReq: python-module-ZODB3
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-collective.indexing
BuildPreReq: python-module-collective.js.showmore
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.contentlisting

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname archetypes.schemaextender collective.indexing Plone
%py_requires collective.js.showmore DateTime plone.app.content unidecode
%py_requires plone.app.controlpanel plone.app.layout plone.browserlayer
%py_requires plone.app.vocabularies plone.indexer Products.Archetypes
%py_requires Products.CMFCore Products.CMFDefault Products.GenericSetup
%py_requires transaction ZODB3 zope.component zope.formlib zope.schema
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires Products.LinguaPlone plone.app.contentlisting

%description
collective.solr integrates the Solr search engine with Plone.

collective.solr comes with a default configuration and setup of Solr
that makes it extremely easy to get started, yet provides a vastly
superior search quality compared to Plone's integrated text search based
on ZCTextIndex.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.solr integrates the Solr search engine with Plone.

collective.solr comes with a default configuration and setup of Solr
that makes it extremely easy to get started, yet provides a vastly
superior search quality compared to Plone's integrated text search based
on ZCTextIndex.

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
%doc *.rst docs/source/*.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150219
- Initial build for Sisyphus

