%define mname collective
%define oname %mname.nitf
Name: python-module-%oname
Version: 2.0
Release: alt1.a1.dev0.git20141226
Summary: A content type inspired on the IPTC's News Industry Text
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.nitf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.nitf.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-robotsuite python-module-openid
BuildPreReq: python-module-collective.js.galleria
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-collective.prettydate
BuildPreReq: python-module-collective.z3cform.widgets
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.lockingbehavior
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.customerize
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-zope.intid

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.formlib zope.i18nmessageid zope.interface zope.schema
%py_requires Products.GenericSetup zope.browserpage zope.component
%py_requires Products.CMFPlone Products.CMFQuickInstallerTool
%py_requires %mname collective.js.galleria collective.js.jqueryui
%py_requires collective.prettydate collective.z3cform.widgets plone.api
%py_requires plone.app.contentmenu plone.app.dexterity plone.app.imaging
%py_requires plone.app.layout plone.app.lockingbehavior plone.dexterity
%py_requires plone.app.portlets plone.app.referenceablebehavior
%py_requires plone.app.registry plone.app.relationfield plone.indexer
%py_requires plone.app.textfield plone.app.vocabularies plone.portlets
%py_requires plone.directives.form plone.formwidget.autocomplete
%py_requires plone.formwidget.contenttree plone.registry plone.uuid

%description
A Dexterity-based content type inspired on the News Industry Text Format
specification.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.collection plone.app.customerize plone.namedfile
%py_requires plone.app.robotframework.testing plone.app.testing
%py_requires plone.browserlayer z3c.relationfield zope.intid
%py_requires plone.testing

%description tests
A Dexterity-based content type inspired on the News Industry Text Format
specification.

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
* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a1.dev0.git20141226
- Initial build for Sisyphus

