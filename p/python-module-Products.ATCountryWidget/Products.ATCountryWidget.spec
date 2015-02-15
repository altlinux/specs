%define oname Products.ATCountryWidget
Name: python-module-%oname
Version: 0.2.6
Release: alt1.git20140307
Summary: A country widget for Archetypes
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ATCountryWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.ATCountryWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone Products.validation Products.CMFCore
%py_requires Products.Archetypes zope.interface

%description
Adds a new tool, portal_countryutil to the Plone root, which lets you
manage a list of areas which may contain several countries from the
official ISO-country list via the ZMI. A complete list of areas and
their countries is being created at install time.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Adds a new tool, portal_countryutil to the Plone root, which lets you
manage a list of areas which may contain several countries from the
official ISO-country list via the ZMI. A complete list of areas and
their countries is being created at install time.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/Products
cp -fR src/Products/ATCountryWidget \
	%buildroot%python_sitelibdir/Products/
cp -fR src/*.egg-info %buildroot%python_sitelibdir/

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
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20140307
- Initial build for Sisyphus

