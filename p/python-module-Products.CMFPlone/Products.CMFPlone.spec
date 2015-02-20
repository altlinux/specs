%define oname Products.CMFPlone
Name: python-module-%oname
Version: 5.0
Release: alt2.b1.dev0.git20150219
Summary: The Plone Content Management System (core)
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFPlone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFPlone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATContentTypes python-module-lxml
BuildPreReq: python-module-mockup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFDiffTool
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.CMFFormController
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.CMFUid
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.ExtendedPathIndex
BuildPreReq: python-module-Products.ExternalEditor
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PasswordResetTool
BuildPreReq: python-module-Products.PlacelessTranslationService
BuildPreReq: python-module-Products.PloneLanguageTool
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.PluginRegistry
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-borg.localrole
BuildPreReq: python-module-five.customerize
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-five.pt
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.customerize
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.app.folder
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.i18n
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.linkintegrity
BuildPreReq: python-module-plone.app.locales
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.redirector
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.search
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.batching
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.intelligenttext
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.outputfilters
BuildPreReq: python-module-plone.portlet.collection
BuildPreReq: python-module-plone.portlet.static
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.schema
BuildPreReq: python-module-plone.session
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plonetheme.barceloneta
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-zope.app.locales
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.structuredtext
BuildPreReq: python-module-zope.tal
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-cssmin
BuildPreReq: python-module-slimit
BuildPreReq: python-module-markdown
BuildPreReq: python-module-ply

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.structuredtext zope.tal zope.tales zope.traversing
%py_requires zope.location zope.pagetemplate zope.publisher zope.site
%py_requires zope.event zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.deferredimport zope.deprecation zope.dottedname
%py_requires zope.app.locales zope.component zope.container mockup
%py_requires plonetheme.barceloneta z3c.autoinclude
%py_requires plone.schema plone.session plone.theme
%py_requires plone.portlets plone.protect plone.registry
%py_requires plone.portlet.collection plone.portlet.static
%py_requires plone.locking plone.memoize plone.outputfilters
%py_requires plone.i18n plone.indexer plone.intelligenttext
%py_requires Products.ATContentTypes Products.CMFCore
%py_requires Products.CMFDefault Products.CMFDiffTool
%py_requires Products.CMFDynamicViewFTI Products.CMFEditions
%py_requires Products.CMFFormController Products.CMFQuickInstallerTool
%py_requires Products.CMFUid Products.contentmigration
%py_requires Products.DCWorkflow Products.ExtendedPathIndex
%py_requires Products.ExternalEditor Products.GenericSetup
%py_requires Products.MimetypesRegistry Products.PasswordResetTool
%py_requires Products.PlacelessTranslationService ZODB3
%py_requires Products.PloneLanguageTool Products.PluggableAuthService
%py_requires Products.PlonePAS markdown
%py_requires Products.PluginRegistry Products.PortalTransforms
%py_requires Products.ResourceRegistries Products.statusmessages
%py_requires borg.localrole five.customerize five.localsitemanager
%py_requires five.pt plone.app.content plone.app.contentlisting
%py_requires plone.app.contentmenu plone.app.contentrules
%py_requires plone.app.contenttypes plone.app.controlpanel
%py_requires plone.app.customerize plone.app.dexterity
%py_requires plone.app.discussion plone.app.folder plone.app.form
%py_requires plone.app.i18n plone.app.jquerytools plone.app.layout
%py_requires plone.app.linkintegrity plone.app.locales plone.app.uuid
%py_requires plone.app.portlets plone.app.redirector plone.app.search
%py_requires plone.app.registry plone.app.theming plone.app.users
%py_requires plone.app.viewletmanager plone.app.vocabularies
%py_requires plone.app.widgets plone.app.workflow plone.batching
%py_requires plone.browserlayer plone.contentrules plone.fieldsets

%description
The core of the Plone content management system.

http://plone.org

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.globalrequest zope.testing plone.app.testing
%py_requires plone.app.robotframework

%description tests
The core of the Plone content management system.

http://plone.org

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
%doc *.rst docs
%_bindir/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/test*
%exclude %python_sitelibdir/Products/*/*/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*
%python_sitelibdir/Products/*/*/*/*/test*

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt2.b1.dev0.git20150219
- New snapshot

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt2.b1.dev0.git20150216
- New snapshot

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt2.b1.dev0.git20141114
- New snapshot

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt2.b1.dev0.git20141102
- Version 5.0b1.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt2.a3.dev0.git20141009
- Added requirement on markdown

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.a3.dev0.git20141009
- Initial build for Sisyphus

