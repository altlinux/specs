%define oname Products.NavigationManager
Name: python-module-%oname
Version: 5.2
Release: alt2
Summary: EEA Navigation Manager skin for EEA
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/products.navigationmanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.EEAPloneAdmin

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFPlone Products.ATContentTypes
%py_requires Products.Archetypes plone.app.contentmenu plone.app.layout
%py_requires plone.app.portlets plone.indexer zope.interface zope.schema
%py_requires zope.lifecycleevent zope.annotation zope.event
%py_requires zope.browsermenu zope.component
%py_requires Products.EEAPloneAdmin

%description
This is a package that generates the portlet navigation for EEA Site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
This is a package that generates the portlet navigation for EEA Site.

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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt2
- Added necessary requirements

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt1
- Initial build for Sisyphus

