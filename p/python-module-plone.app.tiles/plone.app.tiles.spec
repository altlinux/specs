%define mname plone.app
%define oname %mname.tiles
Name: python-module-%oname
Version: 1.1.0
Release: alt1.dev0.git20141102
Summary: Plone UI integration for plone.tiles
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.tiles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.tiles.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-plone.app.blocks
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.drafts

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.annotation zope.i18nmessageid plone.namedfile
%py_requires plone.memoize plone.registry plone.tiles zope.publisher
%py_requires zope.security zope.component zope.interface plone.z3cform
%py_requires plone.app.blocks plone.autoform z3c.form plone.uuid
%py_requires Products.statusmessages zope.traversing zope.event
%py_requires zope.lifecycleevent zope.schema

%description
Plone UI integration for plone.tiles.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.drafts

%description tests
Plone UI integration for plone.tiles.

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
%doc *.txt *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.dev0.git20141102
- Initial build for Sisyphus

