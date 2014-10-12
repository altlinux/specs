%define oname plone.locking
Name: python-module-%oname
Version: 2.0.5
Release: alt1.dev0.git20140826
Summary: webdav locking support
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.locking/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.locking.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.i18nmessageid zope.schema zope.viewlet
%py_requires plone ZODB3 zope.annotation zope.component zope.interface
%py_requires Products.CMFCore

%description
Provides basic automatic locking support for Plone. Locks are stealable
by default, meaning that a user with edit privileges will be able to
steal another user's lock, but will be warned that someone else may be
editing the same object. Used by Plone, Archetypes and
plone.app.iterate.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
#py_requires Products.Archetypes

%description tests
Provides basic automatic locking support for Plone. Locks are stealable
by default, meaning that a user with edit privileges will be able to
steal another user's lock, but will be warned that someone else may be
editing the same object. Used by Plone, Archetypes and
plone.app.iterate.

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
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.dev0.git20140826
- Initial build for Sisyphus

