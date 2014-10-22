%define oname plone.tiles
Name: python-module-%oname
Version: 1.3.0
Release: alt1.dev0.git20140925
Summary: APIs for managing tiles
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.tiles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.tiles.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.app.publisher zope.annotation zope.component
%py_requires zope.configuration zope.interface zope.publisher
%py_requires zope.schema zope.security zope.traversing

%description
plone.tiles implements low-level, non-Plone/Zope2-specific support for
creating "tiles" in the Deco layout system.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing

%description tests
plone.tiles implements low-level, non-Plone/Zope2-specific support for
creating "tiles" in the Deco layout system.

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
nosetests

%files
%doc *.rst
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.dev0.git20140925
- Initial build for Sisyphus

