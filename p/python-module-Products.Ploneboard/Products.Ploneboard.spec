%define oname Products.Ploneboard
Name: python-module-%oname
Version: 3.7
Release: alt1.dev0.git20150207
Summary: A discussion board for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Ploneboard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.Ploneboard.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil python-module-lxml
BuildPreReq: python-module-openid funkload
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.SimpleAttachment
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.SimpleAttachment plone.api
%py_requires plone.app.controlpanel plone.app.portlets plone.portlets
%py_requires plone.memoize plone.i18n Products.CMFPlacefulWorkflow
%py_requires dateutil

%description
Ploneboard is an easy to use web board. It uses the proven Plone user
interface, and is made for easy integration into Plone sites. The target
audience is businesses and developers wanting a discussion board in
their Plone site.

Ploneboard aims to do one thing, and do it well. It will never be an
over-the-top all-bells-and-whistles message board, but will stay minimal
in the sense that it's living inside an existing content management
system - and will leverage that to the fullest extent possible.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing lxml Products.PloneTestCase funkload

%description tests
Ploneboard is an easy to use web board. It uses the proven Plone user
interface, and is made for easy integration into Plone sites. The target
audience is businesses and developers wanting a discussion board in
their Plone site.

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
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/test*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1.dev0.git20150207
- Initial build for Sisyphus

