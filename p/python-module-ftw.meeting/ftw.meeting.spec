%define mname ftw
%define oname %mname.meeting

%def_disable check

Name: python-module-%oname
Version: 1.5.4
Release: alt1.dev0.git20150219
Summary: A meeting content type for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.meeting/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.meeting.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.pdfgenerator
BuildPreReq: python-module-ftw.task
BuildPreReq: python-module-ftw.zipexport
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-ftw.calendarwidget
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.workspace
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.poodle
BuildPreReq: python-module-ftw.calendar
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.pdfgenerator ftw.task ftw.zipexport zope.i18n
%py_requires Products.DataGridField ftw.calendarwidget ftw.upgrade
%py_requires plone.principalsource ftw.workspace ftw.poodle plone.i18n
%py_requires ftw.calendar Products.CMFCore Products.Archetypes
%py_requires Products.ATReferenceBrowserWidget Products.ATContentTypes
%py_requires Products.statusmessages plone.app.layout plone.memoize
%py_requires plone.theme zope.interface zope.component zope.schema
%py_requires zope.i18nmessageid zope.publisher

%description
ftw.meeting provides a meeting content type for plone. The meeting acts
as event but also as meeting report and can contain multiple meeting
items. It provides an ical export and PDF export.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.testbrowser ftw.testing
%py_requires ftw.builder.testing Products.PloneTestCase zope.traversing
%py_requires zope.configuration

%description tests
ftw.meeting provides a meeting content type for plone. The meeting acts
as event but also as meeting report and can contain multiple meeting
items. It provides an ical export and PDF export.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt1.dev0.git20150219
- Initial build for Sisyphus

