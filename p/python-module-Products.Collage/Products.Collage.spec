%define oname Products.Collage
Name: python-module-%oname
Version: 1.3.12
Release: alt1.dev0.git20141117
Summary: A product to create page compositions in Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Collage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.Collage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.i18nmessageid
%py_requires zope.formlib zope.annotation zope.viewlet
%py_requires zope.app.schema zope.schema zope.location zope.i18n
%py_requires zope.interface zope.lifecycleevent zope.component
%py_requires plone.app.controlpanel plone.app.vocabularies zope.event
%py_requires Products.LinguaPlone plone.app.layout plone.memoize
%py_requires Products.ATContentTypes Products.ATReferenceBrowserWidget
%py_requires Products.CMFDefault Products.CMFDynamicViewFTI plone.i18n
%py_requires Products.ZCTextIndex Products.statusmessages plone.protect
%py_requires Products.Archetypes Products.CMFCore Products.CMFPlone

%description
Collage is a product which allows editors to align new or existing
content from multiple sources in a layout. An example of such a page is
one that shows a document along with one or more collections.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.publisher

%description tests
Collage is a product which allows editors to align new or existing
content from multiple sources in a layout. An example of such a page is
one that shows a document along with one or more collections.

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
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.12-alt1.dev0.git20141117
- Initial build for Sisyphus

