%define oname Products.PageCacheManager
Name: python-module-%oname
Version: 1.2.1
Release: alt2.svn20090608
Summary: Cache rendered pages including headers
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PageCacheManager
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.PageCacheManager/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CacheSetup

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore zope.interface
%py_requires Products.CacheSetup

%description
PageCacheManager is designed to speed up access to content views while
at the same time making sure that stale content is not served up.

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

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.svn20090608
- Added necessary requirements

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090608
- Initial build for Sisyphus

