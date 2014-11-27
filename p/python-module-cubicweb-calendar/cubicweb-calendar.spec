%define oname cubicweb-calendar
Name: python-module-%oname
Version: 0.7.0
Release: alt1
Summary: calendar component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-calendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://hg.logilab.org/review/cubes/calendar
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-yams

Requires: cubicweb
%py_requires yams

%description
This cube models calendars with different types of days (working,
non-working, vacation, sick, etc) and time periods (from simple "Aug
31st 2009 to Sep 4th 2009" to repetitive ones like "July 14th").

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

