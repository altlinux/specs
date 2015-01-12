%define oname Products.CMFPlomino
Name: python-module-%oname
Version: 1.19.2
Release: alt1
Summary: Create specific applications in Plone without developing
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFPlomino/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-simplejson python-module-jsonutil
BuildPreReq: python-module-dateutil python-module-selenium
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-collective.js.datatables
BuildPreReq: python-module-collective.codemirror
BuildPreReq: python-module-plomino.tinymce
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.BTreeFolder2
BuildPreReq: python-module-zc.async
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
Requires: python-module-Zope2
%py_requires collective.js.jqueryui collective.js.datatables
%py_requires collective.codemirror plomino.tinymce Products.CMFPlone
%py_requires plone.app.registry plone.app.jquery zope.app.component
%py_requires zope.globalrequest plone.resource Products.CMFCore
%py_requires Products.PluginIndexes Products.ATContentTypes zc.async
%py_requires Products.Archetypes Products.PythonScripts five.formlib
%py_requires Products.DCWorkflow Products.CMFDynamicViewFTI
%py_requires Products.validation Products.ZCatalog Products.ZCTextIndex
%py_requires Products.PortalTransforms Products.BTreeFolder2

%description
Plomino is a powerful and flexible web-based application builder for
Plone.

Features:

* create your own custom applications from a web interface without
  programming
* create and design forms in WYSIWYG mode
* easily embed charts or maps
* create specific actions with formulas (compute fields, send emails,
  ...)
* adapt the application behaviour depending on the user access rights
  and roles
* import/export your application structure and/or your application data,
  including replication between Plomino instances

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing
%py_requires Products.PloneTestCase archetypes.schemaextender

%description tests
Plomino is a powerful and flexible web-based application builder for
Plone.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19.2-alt1
- Version 1.19.2

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19.1-alt1
- Initial build for Sisyphus

