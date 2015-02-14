%define mname uwosh
%define oname %mname.timeslot

%def_disable check

Name: python-module-%oname
Version: 1.5.6
Release: alt1.git20150204
Summary: Make easy signup sheets for office hours and class registrations
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/uwosh.timeslot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/uwosh.timeslot.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.Archetypes Products.CMFPlone plone.i18n
%py_requires zope.i18nmessageid Products.CMFCore Products.validation
%py_requires Products.ATContentTypes plone.app.workflow plone.memoize
%py_requires zope.interface zope.component zope.app.component
%py_requires zope.formlib zope.schema five.formlib

%description
A Plone scheduling product that lets you make easy signup sheets for
office hours and class registrations.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.PloneTestCase

%description tests
A Plone scheduling product that lets you make easy signup sheets for
office hours and class registrations.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt1.git20150204
- Initial build for Sisyphus

