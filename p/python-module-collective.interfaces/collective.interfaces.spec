%define mname collective
%define oname %mname.interfaces
Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20150122
Summary: Adds interfaces tab to Plone's content where Manager's can manage interfaces
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.interfaces/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.interfaces.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-nose
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone Products.CMFCore Products.CMFPlone plone.theme
%py_requires zope.i18nmessageid zope.component zope.interface

%description
Extension for Plone which adds new content view tab to all common
content where Manager can manage marker interfaces on instance level.
Yep, in general this is just Plone UI for "Interfaces" tab available in
the ZMI.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Extension for Plone which adds new content view tab to all common
content where Manager can manage marker interfaces on instance level.
Yep, in general this is just Plone UI for "Interfaces" tab available in
the ZMI.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR %mname/interfaces %buildroot%python_sitelibdir/%mname/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test
nosetests -v

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150122
- Initial build for Sisyphus

