%define mname archetypes
%define oname %mname.kss
Name: python-module-%oname
Version: 1.7.4
Release: alt1.dev0.git20130814
Summary: KSS (Kinetic Style Sheets) for Archetypes
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/archetypes.kss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/archetypes.kss.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-kss.core
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.kss-tests
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.uuid kss.core Products.CMFEditions zope.event
%py_requires Products.CMFPlone Products.CMFCore Products.Archetypes
%py_requires plone.app.kss plone.locking zope.interface zope.component
%py_requires zope.deprecation zope.publisher zope.lifecycleevent

%description
This product gives generic KSS support to Archetypes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase plone.app.kss.tests

%description tests
This product gives generic KSS support to Archetypes.

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
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.dev0.git20130814
- Initial build for Sisyphus

