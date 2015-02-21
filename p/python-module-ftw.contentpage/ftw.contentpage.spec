%define mname ftw
%define oname %mname.contentpage
Name: python-module-%oname
Version: 1.9.1
Release: alt1.dev0.git20150211
Summary: Contentpage based on Simplelayout for for web/intranet
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.contentpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.contentpage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pyquery python-module-openid
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-ftw.calendarwidget
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-ftw.geo
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-ftw.table
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-simplelayout.portlet.dropzone
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-collective.geo.settings
BuildPreReq: python-module-collective.geo.kml
BuildPreReq: python-module-collective.geo.contentlocations
BuildPreReq: python-module-collective.geo.geographer
BuildPreReq: python-module-collective.geo.openlayers
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.formwidget.recaptcha
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.publisher zope.dottedname zope.i18nmessageid plone.api
%py_requires zope.component zope.browserpage zope.interface
%py_requires plone.indexer plone.app.portlets plone.app.blob zope.schema
%py_requires plone.app.imaging plone.portlets plone.z3cform zope.i18n
%py_requires Products.LinguaPlone Products.ATContentTypes plone.registry
%py_requires Products.statusmessages Products.Archetypes plone.memoize
%py_requires Products.CMFPlone Products.ATContentTypes plone.app.layout
%py_requires %mname archetypes.schemaextender collective.quickupload
%py_requires ftw.calendarwidget ftw.colorbox ftw.geo ftw.profilehook
%py_requires ftw.table ftw.upgrade plone.formwidget.contenttree z3c.form
%py_requires simplelayout.base simplelayout.portlet.dropzone plone.i18n
%py_requires collective.geo.settings collective.geo.kml Products.CMFCore
%py_requires collective.geo.contentlocations collective.geo.geographer
%py_requires collective.geo.openlayers collective.geo.mapwidget
%py_requires plone.formwidget.recaptcha plone.dexterity
%py_requires plone.directives.form

%description
ftw.contentpage provides some content types optimized for organisations,
communities, associations, and more.

It uses simplelayout to manage and display the content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing ftw.testbrowser ftw.builder.testing
%py_requires plone.app.testing plone.mocktestcase zope.event
%py_requires zope.configuration zope.viewlet zope.container
%py_requires zope.traversing

%description tests
ftw.contentpage provides some content types optimized for organisations,
communities, associations, and more.

It uses simplelayout to manage and display the content.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1.dev0.git20150211
- Version 1.9.1.dev0

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1.dev0.git20141216
- Version 1.8.7.dev0

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.4-alt1.dev0.git20141120
- Initial build for Sisyphus

