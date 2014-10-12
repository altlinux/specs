%define oname plone.event
Name: python-module-%oname
Version: 1.2
Release: alt1.dev.git20140823
Summary: Event and calendaring related tools not bound to Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.event/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.event.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil python-module-pytz
BuildPreReq: python-module-mock python-module-unittest2
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires plone zope.component zope.interface

%description
Event/Calendaring related infrastructure. Recurrence calculation tools
based on RFC2445 and timedelta recurrence rules, timezone tools and date
conversion tools.

Parts of this package derived from Products.DateRecurringIndex.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.configuration

%description tests
Event/Calendaring related infrastructure. Recurrence calculation tools
based on RFC2445 and timedelta recurrence rules, timezone tools and date
conversion tools.

Parts of this package derived from Products.DateRecurringIndex.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev.git20140823
- Initial build for Sisyphus

