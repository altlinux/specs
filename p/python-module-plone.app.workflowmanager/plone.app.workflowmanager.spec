%define mname plone.app
%define oname %mname.workflowmanager
Name: python-module-%oname
Version: 1.0.2
Release: alt1.dev.git20141028
Summary: A workflow manager for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.workflowmanager-overhaul/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.workflowmanager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-interlude
BuildPreReq: python-module-Zope2-tests python-module-openid
BuildPreReq: python-module-Plone python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone plone.app.jquery Products.DCWorkflow zope.i18n
%py_requires Products.CMFCore plone.app.contentrules plone.contentrules
%py_requires plone.memoize zope.component zope.i18nmessageid zope.schema

%description
This package provides a GUI for managing custom workflows in Plone.

This is the successor of uwosh.northstar's workflow design tool (North*
continues on as a file system product generator, given either a
PloneFormGen or Dexterity prototype).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.keyring zope.interface
%py_requires zope.configuration zope.publisher zope.annotation

%description tests
This package provides a GUI for managing custom workflows in Plone.

This is the successor of uwosh.northstar's workflow design tool (North*
continues on as a file system product generator, given either a
PloneFormGen or Dexterity prototype).

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
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev.git20141028
- Initial build for Sisyphus

