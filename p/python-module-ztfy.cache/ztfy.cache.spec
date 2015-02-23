%define mname ztfy
%define oname %mname.cache
Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: ZTFY package used to handle caches
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-lovely.memcached
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.ramcache
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname lovely.memcached zope.annotation zope.component
%py_requires zope.componentvocabulary zope.configuration zope.container
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.ramcache zope.schema

%description
ZTFY.cache is a small package which provides a common interface to
handle several cache backends.

Currently available backends include Zope native RAM cache and Memcached
cache.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.cache is a small package which provides a common interface to
handle several cache backends.

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
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

