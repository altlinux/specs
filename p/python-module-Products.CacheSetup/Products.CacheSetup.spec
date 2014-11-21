%define oname Products.CacheSetup
Name: python-module-%oname
Version: 1.2.2
Release: alt2.svn20101013
Summary: Control caching of Plone sites
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CacheSetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.CacheSetup/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFSquidTool
BuildPreReq: python-module-Products.PageCacheManager
BuildPreReq: python-module-Products.PolicyHTTPCacheManager
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.StandardCacheManagers
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.tal
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Interface

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.app.publisher zope.component zope.schema zope.event
%py_requires zope.pagetemplate zope.tal zope.publisher zope.tales
%py_requires Products.GenericSetup Products.PythonScripts zope.interface
%py_requires Products.ATContentTypes Products.StandardCacheManagers
%py_requires Products.ResourceRegistries Products.statusmessages
%py_requires Products.Archetypes Products.ZCatalog Products.CMFPlone
%py_requires Products.CMFSquidTool Products.PageCacheManager
%py_requires Products.PolicyHTTPCacheManager Products.CMFCore
%py_requires zope.app.schema zope.deferredimport Interface

%description
CacheFu speeds up Plone sites transparently using a combination of
memory, proxy, and browser caching. Can be used by itself or with Squid,
Varnish, and/or Apache. Once installed, your site should run much faster
(about 10x faster by itself or about 50x faster with Squid).

CacheFu is a collection of products and recipes. The central product is
Products.CacheSetup which takes care of pulling in the rest of the
products from the bundle.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
CacheFu is a collection of products and recipes. The central product is
Products.CacheSetup which takes care of pulling in the rest of the
products from the bundle.

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

install -p -m644 Products/CacheSetup/VERSION.txt \
	%buildroot%python_sitelibdir/Products/CacheSetup/

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
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2.svn20101013
- Added necessary files

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.svn20101013
- Initial build for Sisyphus

