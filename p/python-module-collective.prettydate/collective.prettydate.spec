%define mname collective
%define oname %mname.prettydate
Name: python-module-%oname
Version: 1.2.3
Release: alt1.dev0.git20141112
Summary: Solve some usability issues associated with the utilization of absolute date formating
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.prettydate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.prettydate.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-unittest2
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.component

%py_provides %oname
%py_requires %mname zope.i18nmessageid zope.interface

%description
collective.prettydate is a package that helps developers to solve some
usability issues associated with the utilization of absolute date
formating on sites used among different timezones.

When a date is printed as "01/02/2012" it could represent "February 1"
or "January 2", depending on the format used. Also, if the site is
located on a different timezone, it could take you to situations when
today's date is printed as yesterday, or tomorrow's date.

collective.prettydate represents a date on a relative format so it would
be displayed as "4 hours ago", "yesterday" or "last week", which is
easier to read and understand for most people.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.component

%description tests
collective.prettydate is a package that helps developers to solve some
usability issues associated with the utilization of absolute date
formating on sites used among different timezones.

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
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20141112
- Initial build for Sisyphus

