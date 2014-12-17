%define mname eea
%define oname %mname.progressbar
Name: python-module-%oname
Version: 3.1
Release: alt1
Summary: Progress bar based on current document review_state
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.progressbar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.icons
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-archetypes.schemaextender

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.icons eea.jquery Products.CMFCore plone.portlets
%py_requires Products.GenericSetup Products.statusmessages plone.uuid
%py_requires Products.CMFPlone Products.DCWorkflow Products.Archetypes
%py_requires Products.ZCatalog Products.ATContentTypes plone.app.layout
%py_requires plone.app.controlpanel plone.app.portlets plone.registry
%py_requires plone.app.collection plone.app.contentlisting plone.protect
%py_requires plone.app.form zope.component zope.interface zope.formlib
%py_requires zope.browserpage zope.security zope.configuration zope.i18n
%py_requires zope.schema zope.publisher zope.pagetemplate zope.event
%py_requires zope.i18nmessageid zope.lifecycleevent zope.annotation
%py_requires archetypes.schemaextender

%description
A system that visually display a workflow percentage bar or a workflow
steps trail in the publishing process of a document according with the
workflow state in which the document is. It also define editing progress
(document completion) of an item with customizable labels per field.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
A system that visually display a workflow percentage bar or a workflow
steps trail in the publishing process of a document according with the
workflow state in which the document is. It also define editing progress
(document completion) of an item with customizable labels per field.

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
%doc *.md *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Initial build for Sisyphus

