%define mname collective
%define oname %mname.cover
Name: python-module-%oname
Version: 1.0
Release: alt1.a11.dev0.git20141102
Summary: Editor-friendly way of creating front pages and other composite pages
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.cover/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.cover.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock python-module-openid
BuildPreReq: python-module-collective.js.bootstrap
BuildPreReq: python-module-collective.js.galleria
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.blocks
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.linkintegrity
BuildPreReq: python-module-plone.app.lockingbehavior
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.app.stagingbehavior
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.tiles
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.scale
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.cachepurging
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-grokcore.component-tests
BuildPreReq: python-module-grokcore.annotation-tests
BuildPreReq: python-module-grokcore.security-tests
BuildPreReq: python-module-grokcore.site-tests
BuildPreReq: python-module-grokcore.view-tests
BuildPreReq: python-module-grokcore.viewlet-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.i18nmessageid zope.interface zope.schema
%py_requires z3c.form zope.browserpage zope.component zope.event
%py_requires Products.CMFPlone Products.GenericSetup z3c.caching
%py_requires plone.z3cform Products.Archetypes Products.CMFCore
%py_requires plone.scale plone.supermodel plone.tiles plone.uuid
%py_requires plone.indexer plone.memoize plone.namedfile plone.registry
%py_requires plone.dexterity plone.directives.form plone.i18n
%py_requires plone.app.vocabularies plone.autoform plone.behavior
%py_requires plone.app.textfield plone.app.tiles plone.app.uuid
%py_requires plone.app.relationfield plone.app.stagingbehavior
%py_requires plone.app.lockingbehavior plone.app.referenceablebehavior
%py_requires plone.app.layout plone.app.linkintegrity plone.app.registry
%py_requires plone.app.dexterity plone.app.jquery plone.app.jquerytools
%py_requires collective.js.jqueryui five.grok plone.api plone.app.blocks
%py_requires %mname collective.js.bootstrap collective.js.galleria

%description
collective.cover is a package that allows the creation of elaborate
covers for website homepages, especially for news portals, government
sites and intranets that require more resources than a simple page or
collection can offer. However, despite offering rich resources to build
a cover, collective.cover also provides a very easy mechanism for
managing its contents, built around a drag-and-drop interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing plone.testing
%py_requires plone.browserlayer plone.cachepurging Products.PloneFormGen
%py_requires grokcore.component.testing grokcore.annotation.testing
%py_requires grokcore.security.testing grokcore.site.testing
%py_requires grokcore.view.testing grokcore.viewlet.testing

%description tests
collective.cover is a package that allows the creation of elaborate
covers for website homepages, especially for news portals, government
sites and intranets that require more resources than a simple page or
collection can offer. However, despite offering rich resources to build
a cover, collective.cover also provides a very easy mechanism for
managing its contents, built around a drag-and-drop interface.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a11.dev0.git20141102
- Initial build for Sisyphus

