%define mname plonetheme
%define oname %mname.sunburst
Name: python-module-%oname
Version: 1.5.2
Release: alt1.dev0.git20140710
Summary: The default theme for Plone 4
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonetheme.sunburst/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plonetheme.sunburst.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
%py_requires %mname Products.CMFCore plone.theme zope.component
%py_requires zope.interface

%description
Sunburst is a modern, minimalist, grid-based theme for Plone 4.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.security.testing

%description tests
Sunburst is a modern, minimalist, grid-based theme for Plone 4.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.dev0.git20140710
- Initial build for Sisyphus

