%define mname plone.formwidget
%define oname %mname.datetime
Name: python-module-%oname
Version: 1.1
Release: alt1.dev0.git20141020
Summary: Datetime widgets for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.datetime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.datetime.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone python-module-mock
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-pytz python-module-lxml
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zc.buildout
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone plone.app.jquerytools z3c.form
%py_requires zope.i18nmessageid zope.interface zope.component
%py_requires zope.schema Products.Archetypes Products.CMFCore

%description
The package plone.formwidget.datetime provides date and time widgets for
plone to be used with z3c.form and Archetypes. The calendar widget is
based on JQueryTools Dateinput, provided by plone.app.jquerytools.

The package is a merge of collective.z3cform.datetimewidget and
archetypes.datetimewidget (which itself was derived from
collective.z3cform.datetimewidget).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.ATContentTypes Products.GenericSetup
%py_requires plone.app.testing plone.testing zc.buildout zope.testing
%py_requires zope.app.testing zope.configuration zope.security

%description tests
The package plone.formwidget.datetime provides date and time widgets for
plone to be used with z3c.form and Archetypes. The calendar widget is
based on JQueryTools Dateinput, provided by plone.app.jquerytools.

The package is a merge of collective.z3cform.datetimewidget and
archetypes.datetimewidget (which itself was derived from
collective.z3cform.datetimewidget).

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
%exclude %python_sitelibdir/plone/formwidget/*/test*
%exclude %python_sitelibdir/plone/formwidget/*/*/test*

%files tests
%python_sitelibdir/plone/formwidget/*/test*
%python_sitelibdir/plone/formwidget/*/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev0.git20141020
- Initial build for Sisyphus

