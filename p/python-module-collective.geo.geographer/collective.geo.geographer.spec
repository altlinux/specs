%define mname collective
%define oname %mname.geo.geographer
Name: python-module-%oname
Version: 2.1
Release: alt1.dev0.git20141005
Summary: Geographic annotation for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.geographer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.geographer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.geo Products.CMFCore plone.indexer zope.interface
%py_requires zope.component zope.lifecycleevent zope.annotation
%py_requires zope.event

%description
collective.geo.geographer provides geo annotation for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.geo.geographer provides geo annotation for Plone.

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

rm -f docs/conf.py

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/geo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/geo/*/test*

%files tests
%python_sitelibdir/%mname/geo/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev0.git20141005
- Initial build for Sisyphus

