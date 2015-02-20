%define mname collective.z3cform
%define oname %mname.norobots

%def_disable check

Name: python-module-%oname
Version: 1.4.3
Release: alt1.dev0.git20130425
Summary: Human readable captcha for z3cform
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.norobots/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sylvainb/collective.z3cform.norobots.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-collective.pfg.norobots

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.z3cform plone.app.registry plone.registry
%py_requires Products.CMFCore plone.app.registry zope.interface z3c.form
%py_requires zope.schema zope.component zope.i18nmessageid
%py_requires collective.pfg.norobots

%description
collective.z3cform.norobots provides a "human" captcha widget based on a
list of question/answer(s).

This captcha can be used:

* as a plone.app.discussion (Plone Discussions) captcha plugin
* as a z3c form field
* as a PloneFormGen field with collective.pfg.norobots

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.app.testing plone.app.testing lxml
%py_requires plone.app.caching plone.app.collection plone.app.dexterity

%description tests
collective.z3cform.norobots provides a "human" captcha widget based on a
list of question/answer(s).

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
%python_sitelibdir/collective/z3cform/norobots
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/z3cform/norobots/test*

%files tests
%python_sitelibdir/collective/z3cform/norobots/test*

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.dev0.git20130425
- Initial build for Sisyphus

