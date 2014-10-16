%define oname plone.app.controlpanel

Name: python-module-%oname
Version: 2.4.5
Release: alt2.dev0.git20141009
Summary: Formlib-based controlpanels for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.controlpanel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.controlpanel.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.ramcache
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.app.form plone.app.vocabularies zope.event
%py_requires plone.app.workflow plone.fieldsets plone.memoize zope.i18n
%py_requires plone.protect plone.locking zope.annotation zope.component
%py_requires zope.cachedescriptors zope.formlib zope.interface zope.site
%py_requires zope.ramcache zope.publisher zope.schema zope.testing
%py_requires Products.CMFCore Products.CMFDefault Products.PlonePAS
%py_requires Products.PortalTransforms Products.statusmessages ZODB3
%py_requires Products.CMFPlone

%description
This package provides various control panels for Plone and some
infrastrucuture to make it as easy as possible to create those with the
help of zope.formlib.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase plone.app.testing

%description tests
This package provides various control panels for Plone and some
infrastrucuture to make it as easy as possible to create those with the
help of zope.formlib.

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
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.dev0.git20141009
- Initial build for Sisyphus

