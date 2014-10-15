%define oname plone.app.layout

Name: python-module-%oname
Version: 2.5.2
Release: alt2.dev0.git20141009
Summary: Core visual components for Plone, such as viewlets and general views
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.layout/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.layout.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-plone.app.intid
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-markdown

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.dottedname zope.i18n zope.interface zope.publisher
%py_requires Products.CMFEditions zope.component zope.deprecation
%py_requires plone.registry Products.CMFCore Products.CMFDynamicViewFTI
%py_requires plone.app.viewletmanager plone.memoize plone.portlets
%py_requires plone.app plone.app.content plone.app.portlets plone.i18n
%py_requires zope.schema zope.viewlet
%py_requires Products.CMFPlone

%description
This package contains various visual components for Plone, such as
viewlets and general views.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.intid plone.app.relationfield plone.app.testing
%py_requires plone.dexterity plone.locking plone.testing
%py_requires z3c.relationfield zope.annotation
%py_requires plone.app.contenttypes

%description tests
This package contains various visual components for Plone, such as
viewlets and general views.

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
%exclude %python_sitelibdir/plone/app/*/*/tests

%files tests
%python_sitelibdir/plone/app/*/test*
%python_sitelibdir/plone/app/*/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.dev0.git20141009
- Initial build for Sisyphus

