%define oname plone.app.upgrade

Name: python-module-%oname
Version: 1.3.7
Release: alt2.dev0.git20140920
Summary: Database upgrade steps for the Plone CMS
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.upgrade/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.upgrade.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-borg.localrole
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.session
BuildPreReq: python-module-plone.app.folder
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.ramcache
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFDiffTool
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.CMFUid
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PloneLanguageTool
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-Products.SecureMailHost
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.app.i18n
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.openid
BuildPreReq: python-module-plone.app.redirector
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.theming
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFFormController
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.SecureMailHost Products.ZCatalog
%py_requires Products.PortalTransforms Products.ResourceRegistries
%py_requires Products.PlonePAS Products.PluggableAuthService
%py_requires Products.MimetypesRegistry Products.PloneLanguageTool
%py_requires Products.CMFUid Products.DCWorkflow Products.GenericSetup
%py_requires Products.CMFEditions Products.CMFQuickInstallerTool
%py_requires Products.CMFCore Products.CMFDefault Products.CMFDiffTool
%py_requires zope.ramcache zope.site Products.contentmigration
%py_requires zope.component zope.interface zope.location
%py_requires plone.portlets plone.session plone.app.folder
%py_requires plone.app borg.localrole five.localsitemanager
%py_requires plone.app.portlets Products.CMFPlone Products.Archetypes
%py_requires Products.CMFFormController

%description
This package contains the upgrade machinery to upgrade a Plone site to a
newer version.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFPlacefulWorkflow plone.contentrules
%py_requires plone.app.i18n plone.app.iterate plone.app.openid
%py_requires plone.app.redirector plone.app.viewletmanager
%py_requires plone.app.theming
%py_requires Products.PloneTestCase
%add_python_req_skip alphas

%description tests
This package contains the upgrade machinery to upgrade a Plone site to a
newer version.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*
%exclude %python_sitelibdir/plone/app/*/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*
%python_sitelibdir/plone/app/*/*/test*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt2.dev0.git20140920
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1.dev0.git20140920
- Initial build for Sisyphus

