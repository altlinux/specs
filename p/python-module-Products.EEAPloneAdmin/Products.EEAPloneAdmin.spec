%define oname Products.EEAPloneAdmin

%def_disable check

Name: python-module-%oname
Version: 10.0
Release: alt1
Summary: EEA Plone Admin
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/products.eeaploneadmin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.PloneHelpCenter
BuildPreReq: python-module-eea.translations
BuildPreReq: python-module-Products.NavigationManager
BuildPreReq: python-module-valentine.linguaflow
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-collective.deletepermission
BuildPreReq: python-module-munin.zope
BuildPreReq: python-module-munin.plone
BuildPreReq: python-module-Products.MaildropHost
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.XLIFFMarshall
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-plone.session
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.linkintegrity
BuildPreReq: python-module-plone.cachepurging
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-Products.PloneTestCase
#BuildPreReq: python-module-eea.themecentre
#BuildPreReq: python-module-eea.mediacentre
#BuildPreReq: python-module-eea.reports
#BuildPreReq: python-module-Products.EEAContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.LinguaPlone Products.PloneHelpCenter plone.session
%py_requires eea.translations Products.NavigationManager plone.app.form
%py_requires valentine.linguaflow collective.quickupload plone.app.blob
%py_requires collective.deletepermission munin.zope munin.plone z3c.form
%py_requires Products.MaildropHost Products.ATContentTypes plone.i18n
%py_requires Products.CMFCore Products.GenericSetup Products.CMFPlone
%py_requires Products.statusmessages Products.ZCatalog Products.Marshall
%py_requires Products.CMFQuickInstallerTool Products.PythonScripts
%py_requires Products.XLIFFMarshall Products.Archetypes plone.memoize
%py_requires Products.ZCTextIndex Products.CMFEditions plone.app.caching
%py_requires plone.app.controlpanel plone.app.layout plone.registry
%py_requires plone.app.discussion plone.app.viewletmanager zope.i18n
%py_requires plone.app.imaging plone.app.linkintegrity zope.component
%py_requires plone.cachepurging zope.i18nmessageid zope.publisher
%py_requires zope.interface zope.lifecycleevent zope.event z3c.caching
%py_requires zope.annotation
#py_requires Products.EEAContentTypes

%description
EEAPloneAdmin is a product that adds a customization policy to a Plone
2.1.x portal. The policy contains methods for Plone configuration.

EEAPloneAdmin is based on DIYPloneStyle 1.0.4, a skeleton product ready
for building new graphical designs for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase
#py_requires eea.themecentre eea.mediacentre eea.reports

%description tests
EEAPloneAdmin is a product that adds a customization policy to a Plone
2.1.x portal. The policy contains methods for Plone configuration.

EEAPloneAdmin is based on DIYPloneStyle 1.0.4, a skeleton product ready
for building new graphical designs for Plone.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0-alt1
- Initial build for Sisyphus

