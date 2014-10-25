%define mname collective
%define oname %mname.upload
Name: python-module-%oname
Version: 1.0
Release: alt1.rc2.dev0.git20141024
Summary: File upload widget with multiple file selection, drag&drop support etc.
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.upload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.upload.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok python-module-Pillow
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-robotsuite
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.viewlet

%py_provides %oname
%py_requires %mname five.grok plone.app.content plone.app.contentmenu
%py_requires plone.app.jquery plone.app.jquerytools plone.app.layout
%py_requires plone.app.registry plone.behavior plone.namedfile
%py_requires plone.registry Products.ATContentTypes Products.CMFCore
%py_requires Products.CMFPlone Products.CMFQuickInstallerTool
%py_requires Products.GenericSetup zope.component zope.event
%py_requires zope.interface zope.lifecycleevent zope.schema

%description
File upload widget with multiple file selection, drag&drop support,
progress bars, client-side image resizing and preview images.

collective.upload is smoothly integrated with Plone's UI and works with
any folderish content type based on Archetypes or Dexterity.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.dexterity plone.app.robotframework
%py_requires plone.app.testing plone.browserlayer plone.testing
%py_requires zope.browsermenu zope.viewlet

%description tests
File upload widget with multiple file selection, drag&drop support,
progress bars, client-side image resizing and preview images.

collective.upload is smoothly integrated with Plone's UI and works with
any folderish content type based on Archetypes or Dexterity.

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
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.rc2.dev0.git20141024
- Initial build for Sisyphus

