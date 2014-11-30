%define mname ftw
%define oname %mname.inflator
Name: python-module-%oname
Version: 1.4.1
Release: alt1.dev0.git20141107
Summary: Wizard with content creation and bundle system for predefined configurations
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.inflator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.inflator.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-transmogrify.dexterity
BuildPreReq: python-module-plone.app.multilingual
BuildPreReq: python-module-plone.multilingualbehavior
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.transmogrifier
BuildPreReq: python-module-collective.transmogrifier
BuildPreReq: python-module-collective.blueprint.jsonmigrator
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlacefulWorkflow

%py_provides %oname
Requires: python-module-Zope2
%py_requires collective.blueprint.jsonmigrator ftw.profilehook
%py_requires plone.app.transmogrifier collective.transmogrifier
%py_requires Products.CMFCore Products.CMFPlone Products.GenericSetup
%py_requires zope.schema plone.i18n plone.uuid Products.ATContentTypes
%py_requires zope.dottedname zope.i18nmessageid zope.interface
%py_requires zope.annotation zope.component zope.configuration
%py_requires %mname plone.app.dexterity transmogrify.dexterity ZODB3
%py_requires plone.app.multilingual plone.multilingualbehavior zope.i18n

%description
This packages helps predefining a Plone site setup including content
creation (using generic setup), defining multiple bundles and a wizard
for installing a new site with a bundle.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing zope.configuration plone.testing
%py_requires plone.app.testing Products.CMFPlacefulWorkflow

%description tests
This packages helps predefining a Plone site setup including content
creation (using generic setup), defining multiple bundles and a wizard
for installing a new site with a bundle.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev0.git20141107
- Initial build for Sisyphus

