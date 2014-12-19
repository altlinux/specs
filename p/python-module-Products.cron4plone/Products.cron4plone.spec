%define oname Products.cron4plone
Name: python-module-%oname
Version: 1.1.12
Release: alt1.dev0.git20141019
Summary: cron4plone can do scheduled tasks in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.cron4plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.cron4plone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-unimr.memcachedlock

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone Products.CMFCore Products.CMFDefault plone.memoize
%py_requires Products.CMFPlone Products.PageTemplates zope.interface
%py_requires plone.app.controlpanel zope.site zope.i18nmessageid
%py_requires zope.formlib zope.schema zope.component unimr.memcachedlock

%description
Cron4Plone can do scheduled tasks in Plone, in a syntax very like *NIX
systems' cron daemon. It plugs into Zope's ClockServer machinery.

Optionally cron4plone also uses unimr.memcachedlock to make sure that
only one task is running at a time, even when using a distributed
environment like multiple zeo clients on multiple machines.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Cron4Plone can do scheduled tasks in Plone, in a syntax very like *NIX
systems' cron daemon. It plugs into Zope's ClockServer machinery.

Optionally cron4plone also uses unimr.memcachedlock to make sure that
only one task is running at a time, even when using a distributed
environment like multiple zeo clients on multiple machines.

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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt1.dev0.git20141019
- Initial build for Sisyphus

