%define oname Products.PolicyHTTPCacheManager
Name: python-module-%oname
Version: 1.2.1
Release: alt1.svn20091120
Summary: Cache manager which delegates policy to CMF's caching policy manager
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PolicyHTTPCacheManager
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.PolicyHTTPCacheManager/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFTestCase
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore zope.interface

%description
* Delegates the setting of cache-related HTTP headers to CMF's Caching
  Policy Manager.
* Will remove a previously set Last-Modified header set by code inside
  Zope if you ask it to.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFTestCase zope.testing

%description tests
Cache manager which delegates policy to CMF's caching policy manager.

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
py.test

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20091120
- Initial build for Sisyphus

