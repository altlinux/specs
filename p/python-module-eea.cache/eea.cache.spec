%define mname eea
%define oname %mname.cache
Name: python-module-%oname
Version: 7.3
Release: alt1.dev.git20141120
Summary: Easy use memcached cache with Zope and Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.cache.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-memcached
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname memcache plone.memoize plone.uuid Products.CMFCore
%py_requires Products.statusmessages plone.app.caching plone.autoform
%py_requires plone.supermodel zope.interface zope.component zope.schema
%py_requires zope.event zope.i18nmessageid z3c.form

%description
This package combines the features from lovely.memcached and
plone.memoize.ram. It provides a decorator and utility for Memcaches at
EEA. The decorator allows you set dependencies known by eea.cache.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration zope.testing

%description tests
This package combines the features from lovely.memcached and
plone.memoize.ram. It provides a decorator and utility for Memcaches at
EEA. The decorator allows you set dependencies known by eea.cache.

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

pushd %mname/cache
cp -fR *.txt *.zcml Extensions documentation profiles \
	%buildroot%python_sitelibdir/%mname/cache/
install -p -m644 browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/cache/browser/
install -p -m644 subtypes/*.zcml \
	%buildroot%python_sitelibdir/%mname/cache/subtypes/
popd

%check
python setup.py test

%files
%doc *.md *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3-alt1.dev.git20141120
- Initial build for Sisyphus

