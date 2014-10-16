%define mname plone.formwidget
%define oname %mname.recurrence

Name: python-module-%oname
Version: 1.2.6
Release: alt2.dev0.git20140823
Summary: Recurrence widget for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.recurrence/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.recurrence.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
%py_requires %mname Products.CMFCore zope.component zope.i18n z3c.form
%py_requires zope.i18nmessageid zope.interface zope.schema
%py_requires zope.traversing Products.validation
%py_requires Products.CMFPlone Products.Archetypes

%description
The plone.formwidget.recurrence package provides an Archetype and a
z3cform widget for recurrence.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.GenericSetup plone.app.testing plone.app.z3cform
%py_requires Products.ATContentTypes

%description tests
The plone.formwidget.recurrence package provides an Archetype and a
z3cform widget for recurrence.

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
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/tests

%files tests
%python_sitelibdir/plone/formwidget/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev0.git20140823
- Initial build for Sisyphus

