%define mname collective
%define oname %mname.base
Name: python-module-%oname
Version: 0.7
Release: alt1.git20131111
Summary: Base class for plone with commonly used methods
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/taito/collective.base.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone Products.CMFCore plone.memoize
%py_requires plone.app.contentlisting plone.app.layout zope.interface
%py_requires plone.app.viewletmanager zope.viewlet

%description
collective.base provides base class for adapter with commonly used
methods.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock plone.app.testing Products.PlonePAS
%py_requires Products.ATContentTypes

%description tests
collective.base provides base class for adapter with commonly used
methods.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20131111
- Initial build for Sisyphus

