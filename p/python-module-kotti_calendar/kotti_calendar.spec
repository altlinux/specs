%define oname kotti_calendar
Name: python-module-%oname
Version: 0.9.0
Release: alt1.dev.git20150107
Summary: Add a calendar to your Kotti site
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_calendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/kotti_calendar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-js.fullcalendar python-module-pytest-cov
BuildPreReq: python-module-webtest python-module-zope.testbrowser
BuildPreReq: python-module-fanstatic python-module-pyramid
BuildPreReq: python-module-SQLAlchemy

%py_provides %oname
%py_requires kotti js.fullcalendar fanstatic pyramid sqlalchemy
# for tests:
%py_requires webtest

%description
This is an extension to the Kotti CMS that allows you to add calendars
with events to your Kotti site.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.dev.git20150107
- Initial build for Sisyphus

