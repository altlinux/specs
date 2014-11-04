%define mname collective
%define oname %mname.mediaelementjs
Name: python-module-%oname
Version: 0.4.3
Release: alt1.dev0.git20141103
Summary: A simple integration of the MediaElementJS video player for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.mediaelementjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.mediaelementjs.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-hachoir-core
BuildPreReq: python-module-hachoir-metadata python-module-hachoir-parser
BuildPreReq: python-module-Zope2-tests python-module-interlude
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-nose
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.cachedescriptors
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.Archetypes Products.ATContentTypes ZODB3
%py_requires Products.CMFCore Products.GenericSetup plone.app.jquery
%py_requires plone.rfc822 zope.annotation zope.cachedescriptors
%py_requires zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
An integration of the MediaElementJS audio and video player for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testcaselayer Products.PloneTestCase

%description tests
An integration of the MediaElementJS audio and video player for Plone.

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
nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.dev0.git20141103
- Initial build for Sisyphus

