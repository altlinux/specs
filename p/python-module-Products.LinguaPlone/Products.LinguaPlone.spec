%define oname Products.LinguaPlone
Name: python-module-%oname
Version: 4.1.4
Release: alt1.dev0.git20140817
Summary: Manage and maintain multilingual content that integrates seamlessly with Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.LinguaPlone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.LinguaPlone.git 
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PloneLanguageTool
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.i18n
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.ATContentTypes
%py_requires Products.CMFCore Products.CMFDynamicViewFTI
%py_requires Products.CMFPlone Products.GenericSetup ZODB3
%py_requires Products.PloneLanguageTool Products.PloneTestCase
%py_requires Products.statusmessages Products.ZCTextIndex zope.interface
%py_requires plone.browserlayer plone.i18n plone.indexer zope.formlib
%py_requires plone.locking plone.memoize plone.theme plone.app.caching
%py_requires plone.app.controlpanel plone.app.i18n plone.app.iterate
%py_requires plone.app.layout plone.app.portlets zope.component
%py_requires zope.i18nmessageid zope.schema zope.site

%description
LinguaPlone is the multilingual/translation solution for Plone, and
achieves this by being as transparent as possible and by minimizing the
impact for existing applications and Plone itself.

It utilizes the Archetypes reference engine to do the translation, and
all content is left intact both on install and uninstall - thus, it will
not disrupt your content structure in any way.

LinguaPlone doesn't require a particular hierarchy of content, and will
in theory work with any layout of your content space, though the default
layout advertised in the install instructions will make the site easier
to use.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing

%description tests
LinguaPlone is the multilingual/translation solution for Plone, and
achieves this by being as transparent as possible and by minimizing the
impact for existing applications and Plone itself.

It utilizes the Archetypes reference engine to do the translation, and
all content is left intact both on install and uninstall - thus, it will
not disrupt your content structure in any way.

LinguaPlone doesn't require a particular hierarchy of content, and will
in theory work with any layout of your content space, though the default
layout advertised in the install instructions will make the site easier
to use.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1.dev0.git20140817
- Initial build for Sisyphus

