%define mname collective.js
%define oname %mname.underscore
Name: python-module-%oname
Version: 1.5.2
Release: alt1.git20140122
Summary: underscore.js for plone
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.underscore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.underscore.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires %mname

%description
Bundles underscore.js for use with Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing zope.component.testing
%py_requires zope.security.testing

%description tests
Bundles underscore.js for use with Plone.

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
%doc *.txt docs/*
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/js/*/tests.*

%files tests
%python_sitelibdir/collective/js/*/tests.*

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140122
- Initial build for Sisyphus

