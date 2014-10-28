%define mname collective
%define oname %mname.signupsheet
Name: python-module-%oname
Version: 0.2.1
Release: alt1.dev0.git20141027
Summary: A Plone solution for manage signup attendance to events
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.signupsheet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.signupsheet.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-collective.js.knockout
BuildPreReq: python-module-uwosh.pfg.d2c
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.CMFPlone-tests

%py_provides %oname
%py_requires %mname Products.PloneFormGen collective.js.knockout
%py_requires uwosh.pfg.d2c

%description
A signup sheet implementation for Plone. New events-like content are
added to your site, users can subscribe to those events filling a
customizable form.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.security.testing
%py_requires Products.CMFPlone.tests

%description tests
A signup sheet implementation for Plone. New events-like content are
added to your site, users can subscribe to those events filling a
customizable form.

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
%doc *.rst *.md docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.dev0.git20141027
- Initial build for Sisyphus

