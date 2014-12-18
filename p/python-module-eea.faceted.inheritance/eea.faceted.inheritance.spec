%define mname eea.faceted
%define oname %mname.inheritance
Name: python-module-%oname
Version: 4.6
Release: alt1
Summary: Allow a faceted navigable object to inherit faceted configuration from another object
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.faceted.inheritance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.facetednavigation Products.statusmessages
%py_requires Products.CMFCore Products.GenericSetup zope.component
%py_requires zope.interface zope.event zope.schema zope.annotation

%description
An extension to be used within eea.facetednavigation in order to allow
objects to inherit faceted configuration from another faceted navigable
object. This way one can define a global faceted navigable folder and
reuse this configuration for multiple heritors.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
An extension to be used within eea.facetednavigation in order to allow
objects to inherit faceted configuration from another faceted navigable
object. This way one can define a global faceted navigable folder and
reuse this configuration for multiple heritors.

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
%python_sitelibdir/eea/faceted/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/eea/faceted/*/tests

%files tests
%python_sitelibdir/eea/faceted/*/tests

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1
- Initial build for Sisyphus

