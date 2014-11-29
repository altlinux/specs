%define mname collective
%define oname %mname.geo.openlayers
Name: python-module-%oname
Version: 3.2
Release: alt1.dev0.git20140226
Summary: Openlayers support for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.openlayers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.openlayers.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component

%py_provides %oname
%py_requires %mname.geo Products.CMFCore zope.interface zope.component

%description
collective.geo.openlayers enables Openlayers machinery into Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
collective.geo.openlayers enables Openlayers machinery into Plone.

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
%python_sitelibdir/%mname/geo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/geo/*/test*

%files tests
%python_sitelibdir/%mname/geo/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.dev0.git20140226
- Initial build for Sisyphus

