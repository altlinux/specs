%define mname ftw
%define oname %mname.upgrade
Name: python-module-%oname
Version: 1.11.0
Release: alt1.dev0.git20141209
Summary: An upgrade control panel and upgrade helpers for plone upgrades
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.upgrade/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.upgrade.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-tarjan python-module-transaction
BuildPreReq: python-module-unittest2 python-module-mocker
BuildPreReq: python-module-argcomplete python-module-argparse
BuildPreReq: python-module-inflection python-module-path
BuildPreReq: python-module-Products.BTreeFolder2
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-zc.recipe.egg

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.BTreeFolder2 Products.ZCatalog zope.component
%py_requires zope.interface zope.publisher Products.GenericSetup
%py_requires plone.browserlayer Products.CMFCore Products.CMFPlone

%description
This product aims to simplify running and writing third-party Generic
Setup upgrade steps in Plone.

It provides a control panel for running multiple upgrades at once, based
on the upgrade mechanism of Generic Setup (portal_setup).

Further a base class for writing upgrade steps with a variety of helpers
for common tasks is provided.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing ftw.testbrowser plone.testing zc.recipe.egg
%py_requires plone.app.testing zope.configuration ftw.builder.testing
%py_requires Products.ATContentTypes Products.CMFPlacefulWorkflow

%description tests
This product aims to simplify running and writing third-party Generic
Setup upgrade steps in Plone.

It provides a control panel for running multiple upgrades at once, based
on the upgrade mechanism of Generic Setup (portal_setup).

Further a base class for writing upgrade steps with a variety of helpers
for common tasks is provided.

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
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.dev0.git20141209
- Version 1.11.0.dev0

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.3-alt1.dev0.git20141126
- Initial build for Sisyphus

