%define mname collective.z3cform
%define oname %mname.widgets
Name: python-module-%oname
Version: 1.0
Release: alt1.b12.dev0.git20141127
Summary: A widget package for Dexterity projects
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.widgets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.widgets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-robotsuite

%py_provides %oname
%py_requires %mname collective.js.jqueryui plone.app.dexterity
%py_requires plone.app.layout plone.app.vocabularies plone.autoform
%py_requires plone.dexterity plone.directives.form Products.CMFCore
%py_requires plone.formwidget.autocomplete plone.formwidget.contenttree
%py_requires Products.CMFPlone Products.GenericSetup z3c.form
%py_requires zope.browserpage zope.component zope.i18nmessageid
%py_requires zope.interface

%description
A widget package for Dexterity projects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework.testing plone.app.testing
%py_requires plone.browserlayer plone.z3cform plone.testing

%description tests
A widget package for Dexterity projects.

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
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/z3cform/*/test*

%files tests
%python_sitelibdir/collective/z3cform/*/test*

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b12.dev0.git20141127
- Initial build for Sisyphus

