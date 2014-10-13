%define oname plone.browserlayer
Name: python-module-%oname
Version: 2.1.4
Release: alt1.dev0.git20140823
Summary: Browser layer management for Zope 2 applications
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.browserlayer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.browserlayer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.component zope.interface zope.traversing
%py_requires Products.CMFCore Products.GenericSetup

%description
This package aims to make it easier to register visual components (e.g.
views and viewlets) so that they only show up in a Plone site where they
have been explicitly installed.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package aims to make it easier to register visual components (e.g.
views and viewlets) so that they only show up in a Plone site where they
have been explicitly installed.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1.dev0.git20140823
- Initial build for Sisyphus

