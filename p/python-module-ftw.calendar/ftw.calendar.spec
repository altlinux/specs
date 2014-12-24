%define mname ftw
%define oname %mname.calendar
Name: python-module-%oname
Version: 2.0.1
Release: alt1.dev0.git20141107
Summary: Calendar view based on fullcalendar
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.calendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.calendar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-simplejson
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore zope.interface zope.component
%py_requires zope.i18nmessageid

%description
ftw.calendar is a calendar view based on fullcalendar
(http://arshaw.com/fullcalendar).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing ftw.builder.testing plone.app.testing
%py_requires ftw.testbrowser zope.configuration

%description tests
ftw.calendar is a calendar view based on fullcalendar
(http://arshaw.com/fullcalendar).

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
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.dev0.git20141107
- Initial build for Sisyphus

