%define oname Products.ContentWellPortlets
Name: python-module-%oname
Version: 4.3.0
Release: alt1.dev0.git20141118
Summary: A Plone product that enables you to add portlets to the central column in a page
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ContentWellPortlets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.ContentWellPortlets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.browserlayer

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.CMFCore plone.app.portlets
%py_requires plone.portlets plone.app.layout plone.app.controlpanel
%py_requires zope.interface zope.component zope.publisher
%py_requires zope.i18nmessageid

%description
A Plone product that enables you to add portlets to the central column
in a page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase plone.browserlayer

%description tests
A Plone product that enables you to add portlets to the central column
in a page.

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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.dev0.git20141118
- Initial build for Sisyphus

