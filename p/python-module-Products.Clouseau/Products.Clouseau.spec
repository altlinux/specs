%define oname Products.Clouseau
Name: python-module-%oname
Version: 1.0
Release: alt1.svn20110505
Summary: An Ajax based Zope/Python prompt for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Clouseau/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.Clouseau/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.DocFinderTab
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.DocFinderTab Products.CMFCore

%description
Clouseau is an Ajax based Zope/Python prompt. Think of it as a
replacement for zopectl debug. A Python prompt that allows you to
interact with your Zope site. It does this with an Ajax interface, so
you can do this right from Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFPlone zope.component.testing
%py_requires zope.security.testing Products.CMFPlone.tests

%description tests
Clouseau is an Ajax based Zope/Python prompt. Think of it as a
replacement for zopectl debug. A Python prompt that allows you to
interact with your Zope site. It does this with an Ajax interface, so
you can do this right from Plone.

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
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20110505
- Initial build for Sisyphus

