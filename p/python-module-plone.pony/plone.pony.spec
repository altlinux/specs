%define oname plone.pony
Name: python-module-%oname
Version: 1.3
Release: alt1.svn20081011
Summary: A pony for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.pony/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/plone/plone.pony/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires plone.theme

%description
Django's got a pony now, so hey...

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.Five zope.testing
%py_requires zope.component.testing zope.security.testing

%description tests
Django's got a pony now, so hey...

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
rm -fR build
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20081011
- Initial build for Sisyphus

