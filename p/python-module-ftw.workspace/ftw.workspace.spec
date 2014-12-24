%define mname ftw
%define oname %mname.workspace

%def_disable check

Name: python-module-%oname
Version: 3.0.2
Release: alt1.dev0.git20141119
Summary: A project folder for plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.workspace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.workspace.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pyquery python-module-openid
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-collective.js.jqsmartTruncation
BuildPreReq: python-module-ftw.activity
BuildPreReq: python-module-ftw.calendar
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-ftw.tabbedview
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-ftw.pdfgenerator-tests
BuildPreReq: python-module-ftw.file
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.batching
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname z3c.relationfield collective.js.jqsmartTruncation
%py_requires ftw.activity ftw.calendar ftw.colorbox ftw.tabbedview
%py_requires ftw.upgrade plone.formwidget.contenttree plone.namedfile
%py_requires plone.principalsource ftw.pdfgenerator ftw.file plone.i18n
%py_requires Products.CMFPlone Products.CMFCore Products.statusmessages
%py_requires Products.MimetypesRegistry Products.Archetypes zope.schema
%py_requires Products.ATContentTypes Products.ZCatalog plone.registry
%py_requires plone.z3cform plone.batching plone.memoize plone.app.blob
%py_requires plone.indexer zope.component zope.container zope.publisher
%py_requires zope.i18nmessageid zope.i18n z3c.form

%description
ftw.workspace provides a project folder for plone.

The folder has a tabbed view with the tabs:

* Overview: Shows recently modified contents within this workspace and
  the structure (subfolders)
* Documents: Lists files recursively
* Events: Lists events (see ftw.meeting) and a calendar view.

The @@workspaces_view lists all workspaces recursively.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.quickupload plone.app.testing ftw.testing
%py_requires ftw.testbrowser ftw.builder.testing zope.traversing
%py_requires zope.configuration ftw.pdfgenerator.tests

%description tests
ftw.workspace provides a project folder for plone.

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.dev0.git20141119
- Initial build for Sisyphus

