%define mname ftw
%define oname %mname.table
Name: python-module-%oname
Version: 1.15.3
Release: alt1.dev0.git20141107
Summary: Table generator utility for use within zope
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.table/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.table.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-cssselect
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-collective.js.extjs
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires five.globalrequest ftw.upgrade collective.js.extjs
%py_requires Products.CMFCore Products.ATContentTypes Products.CMFPlone
%py_requires Products.ZCTextIndex plone.memoize zope.app.component
%py_requires zope.component zope.i18n zope.i18nmessageid zope.schema
%py_requires zope.interface zope.globalrequest

%description
The ftw.table package provides a utility for generating HTML tables of
dicts, catalog brains and other objects.

It comes with a jQuery plugin installable with a Plone Generic Setup
profile, providing features such as sorting, filter, grouping checkboxes
and more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testing plone.app.testing
%py_requires plone.mocktestcase zope.configuration

%description tests
The ftw.table package provides a utility for generating HTML tables of
dicts, catalog brains and other objects.

It comes with a jQuery plugin installable with a Plone Generic Setup
profile, providing features such as sorting, filter, grouping checkboxes
and more.

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
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.3-alt1.dev0.git20141107
- Initial build for Sisyphus

