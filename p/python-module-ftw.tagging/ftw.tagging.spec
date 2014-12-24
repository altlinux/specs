%define mname ftw
%define oname %mname.tagging
Name: python-module-%oname
Version: 1.1.2
Release: alt1.dev0.git20141107
Summary: Tagging add-on for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.tagging/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.tagging.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.AddRemoveWidget
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-ftw.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.component zope.formlib zope.i18nmessageid
%py_requires zope.interface zope.schema archetypes.schemaextender
%py_requires Products.AddRemoveWidget Products.Archetypes plone.portlets
%py_requires Products.CMFCore Products.CMFPlone plone.app.layout
%py_requires plone.app.portlets plone.theme

%description
ftw.tagging extends Plone content types with a tags field using
schemaextender. Further it's possible to define tag roots to restrict
tags to a part of the site.

A tag cloud portlet is provided that shows a tag cloud for the current
tag root.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testcaselayer Products.PloneTestCase ftw.testing

%description tests
ftw.tagging extends Plone content types with a tags field using
schemaextender. Further it's possible to define tag roots to restrict
tags to a part of the site.

A tag cloud portlet is provided that shows a tag cloud for the current
tag root.

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
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.dev0.git20141107
- Initial build for Sisyphus

