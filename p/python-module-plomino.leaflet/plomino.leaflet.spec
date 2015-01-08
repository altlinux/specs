%define mname plomino
%define oname %mname.leaflet
Name: python-module-%oname
Version: 0.2
Release: alt1.dev.git20130207
Summary: Leaflet/Plomino integration
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plomino.leaflet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plomino/plomino.leaflet.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openid
BuildPreReq: python-module-Products.CMFPlomino
BuildPreReq: python-module-collective.js.leaflet
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlomino collective.js.leaflet
%py_requires zope.pagetemplate zope.schema zope.component zope.interface
%py_requires zope.formlib

%description
plomino.leaflet provides a Leaflet map field type to Plomino.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
plomino.leaflet provides a Leaflet map field type to Plomino.

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
py.test %mname/leaflet/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev.git20130207
- Initial build for Sisyphus

