%define oname Products.eeawebapplication
Name: python-module-%oname
Version: 4.3
Release: alt1
Summary: EEA Web Application skin for EEA
License: GPLv2+
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/products.eeawebapplication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.CMFCore plone.app.portlets
%py_requires plone.app.layout zope.interface zope.component

%description
This product provides templates for folders marked with
IEEAWebApplication interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.CMFPlone.tests

%description tests
This product provides templates for folders marked with
IEEAWebApplication interface.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1
- Initial build for Sisyphus

