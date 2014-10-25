%define mname collective.contact
%define oname %mname.core
Name: python-module-%oname
Version: 1.4
Release: alt1.dev0.git20140929
Summary: Core package for collective.contact add-ons
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.contact.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.contact.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ExtensionClass
BuildPreReq: python-module-collective.z3cform.datagridfield
BuildPreReq: python-module-collective.contact.widget
BuildPreReq: python-module-ecreall.helpers.upgrade
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.linkintegrity
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.formwidget.datetime
BuildPreReq: python-module-plone.formwidget.masterselect
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-vobject
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires %mname collective.z3cform.datagridfield five.grok
%py_requires collective.contact.widget ecreall.helpers.upgrade
%py_requires five.globalrequest plone.api plone.app.dexterity
%py_requires plone.app.linkintegrity plone.app.relationfield
%py_requires plone.autoform plone.formwidget.datetime plone.supermodel
%py_requires plone.formwidget.masterselect Products.CMFPlone
%py_requires zope.schema

%description
A Plone add-on that provides a directory where you create persons,
organizations, sub-organizations and positions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework
%py_requires ecreall.helpers.testing plone.app.robotframework.testing

%description tests
A Plone add-on that provides a directory where you create persons,
organizations, sub-organizations and positions.

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
%python_sitelibdir/collective/contact/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/contact/*/test*
%exclude %python_sitelibdir/collective/contact/*/*/test*

%files tests
%python_sitelibdir/collective/contact/*/test*
%python_sitelibdir/collective/contact/*/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev0.git20140929
- Initial build for Sisyphus

