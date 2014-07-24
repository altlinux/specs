%define oname plone.memoize

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt4
Summary: Decorators for caching the values of functions and methods
License: GPLv2
Group: Development/Python
Url: http://pypi.python.org/pypi/plone.memoize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: Decorators for caching the values of functions and methods
Group: Development/Python3
%py3_requires plone zope.annotation zope.component zope.interface
%py3_requires zope.ramcache

%description -n python3-module-%oname
plone.memoize provides Python function decorators for caching the values
of functions and methods.

The type of cache storage is freely configurable by the user, as is the
cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages. It also has specialized decorators for use with
Zope views. However, plone.memoize can be used without Zope.

%package -n python3-module-%oname-tests
Summary: Tests for plone.memoize
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration zope.publisher zope.testing

%description -n python3-module-%oname-tests
plone.memoize provides Python function decorators for caching the values
of functions and methods.

The type of cache storage is freely configurable by the user, as is the
cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages. It also has specialized decorators for use with
Zope views. However, plone.memoize can be used without Zope.

This package contains tests for plone.memoize.

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

%package -n python3-module-plone
Summary: Core files for plone
Group: Development/Python3

%description -n python3-module-plone
Core files for plone.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
touch %buildroot%python_sitelibdir/plone/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/plone/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/plone/__init__.py
%exclude %python3_sitelibdir/plone/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-plone
%python3_sitelibdir/plone/__init__.py
%python3_sitelibdir/plone/__pycache__/__init__.*
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt3.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Fixed requirements

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

