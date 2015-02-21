%define oname Products.ATContentTypes

Name: python-module-%oname
Version: 2.2.3
Release: alt1.dev0.git20150126
Summary: Core content types for Plone 2.1 - 4.3
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ATContentTypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.ATContentTypes.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.folder
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.tal
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFFormController
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PortalTransforms Products.validation ZODB3
%py_requires Products.GenericSetup Products.MimetypesRegistry
%py_requires Products.CMFDefault transaction zope.container zope.event
%py_requires zope.publisher Products.CMFCore Products.CMFDynamicViewFTI
%py_requires zope.component zope.i18n zope.i18nmessageid zope.interface
%py_requires plone.app.collection plone.app.folder plone.app.widgets
%py_requires plone.i18n plone.memoize plone.app.blob plone.app.layout
%py_requires Products.CMFPlone Products.Archetypes zope.lifecycleevent
%py_requires Products.CMFFormController

%description
Default Content Types for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.annotation zope.testing plone.app.testing
%py_requires Products.PloneTestCase
%add_python_req_skip exif

%description tests
Default Content Types for Plone.

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
%doc *.txt docs
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/tests

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/tests

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1.dev0.git20150126
- New snapshot

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1.dev0.git20141023
- Version 2.2.3.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.dev0.git20141009
- Initial build for Sisyphus

