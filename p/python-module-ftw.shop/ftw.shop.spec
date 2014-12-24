%define mname ftw
%define oname %mname.shop

%def_disable check

Name: python-module-%oname
Version: 2.0.4
Release: alt1.dev0.git20141107
Summary: A web shop solution for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.shop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.shop.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-argparse
BuildPreReq: python-module-simplejson python-module-pyquery
BuildPreReq: python-module-openid
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-collective.z3cform.wizard
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
%py_requires %mname collective.js.jqueryui collective.z3cform.wizard
%py_requires ftw.upgrade plone.api plone.app.registry plone.app.z3cform
%py_requires Products.CMFPlone Products.CMFCore Products.statusmessages
%py_requires Products.Archetypes Products.LinguaPlone
%py_requires Products.ATContentTypes

%description
ftw.shop is a general purpose web shop product for Plone. It features
item variations, an extensible checkout wizard, pluggable payment
processors and optional SQLAlchemy storage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase ftw.builder.testing ftw.testbrowser
%py_requires ftw.testing plone.app.testing zope.testing
%py_requires Products.CMFPlone.tests

%description tests
ftw.shop is a general purpose web shop product for Plone. It features
item variations, an extensible checkout wizard, pluggable payment
processors and optional SQLAlchemy storage.

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.dev0.git20141107
- Initial build for Sisyphus

