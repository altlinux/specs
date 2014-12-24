%define mname collective
%define oname %mname.lastmodifier
Name: python-module-%oname
Version: 1.1.3
Release: alt1.dev0.git20141107
Summary: Extends Plone content with metadata about the last modifier
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.lastmodifier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/collective.lastmodifier.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent

%py_provides %oname
%py_requires %mname Products.Archetypes Products.CMFCore ftw.profilehook
%py_requires Products.CMFPlone Products.GenericSetup plone.indexer
%py_requires archetypes.schemaextender collective.monkeypatcher
%py_requires zope.interface

%description
collective.lastmodifier provides support for storing the user who made
the last modification on a content item. It extends Archetypes-based
content types with a lastModifier field using schemaextender. Further it
registers an index and a metadata column in portal_catalog and enables
their usage in collections.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testing plone.app.dexterity
%py_requires plone.app.testing plone.directives.form zope.event
%py_requires zope.lifecycleevent

%description tests
collective.lastmodifier provides support for storing the user who made
the last modification on a content item. It extends Archetypes-based
content types with a lastModifier field using schemaextender. Further it
registers an index and a metadata column in portal_catalog and enables
their usage in collections.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141107
- Initial build for Sisyphus

