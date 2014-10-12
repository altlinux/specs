%define oname Products.DateRecurringIndex
Name: python-module-%oname
Version: 2.1.1
Release: alt1.dev0.git20140302
Summary: Zope 2 date index with support for recurring events
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.DateRecurringIndex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.DateRecurringIndex.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pytz python-module-docutils
BuildPreReq: python-module-plone.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3 plone.event zope.interface zope.schema

%description
A Zope 2 catalog index with support for indexing of recurring events,
following the icalendar standard. It is a drop-in replacement for the
Zope2 DateIndex and will produce the same results for non-recurring
dates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing

%description tests
A Zope 2 catalog index with support for indexing of recurring events,
following the icalendar standard. It is a drop-in replacement for the
Zope2 DateIndex and will produce the same results for non-recurring
dates.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.dev0.git20140302
- Initial build for Sisyphus

