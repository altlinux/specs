%define oname plone.memoize
Name: python-module-%oname
Version: 1.1.1
Release: alt3.1
Summary: Decorators for caching the values of functions and methods
License: GPLv2
Group: Development/Python
Url: http://pypi.python.org/pypi/plone.memoize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires plone zope.annotation zope.component zope.interface
%py_requires zope.ramcache

%description
plone.memoize provides Python function decorators for caching the values
of functions and methods.

The type of cache storage is freely configurable by the user, as is the
cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages. It also has specialized decorators for use with
Zope views. However, plone.memoize can be used without Zope.

%package tests
Summary: Tests for plone.memoize
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.publisher zope.testing

%description tests
plone.memoize provides Python function decorators for caching the values
of functions and methods.

The type of cache storage is freely configurable by the user, as is the
cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages. It also has specialized decorators for use with
Zope views. However, plone.memoize can be used without Zope.

This package contains tests for plone.memoize.

%package -n python-module-plone
Summary: Core files for plone
Group: Development/Python

%description -n python-module-plone
Core files for plone.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

touch %buildroot%python_sitelibdir/plone/__init__.py

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/plone/__init__.py*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python-module-plone
%python_sitelibdir/plone/__init__.py*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Fixed requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

