%define mname collective
%define oname %mname.taskqueue
Name: python-module-%oname
Version: 0.7.2
Release: alt1.dev0.git20150126
Summary: Yet another way to queue and execute asynchronous tasks in Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.taskqueue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.taskqueue.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-redis-py python-module-msgpack
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-z3c.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname five.globalrequest redis msgpack Products.CMFCore
%py_requires Products.PluggableAuthService Products.PlonePAS zope.schema
%py_requires plone.memoize zope.component zope.interface
%py_requires zope.globalrequest

%description
collective.taskqueue enables asynchronous tasks in Plone add-ons by
providing a small framework for asynchronously queueing requests to
ZPublisher. With this aproachasynchronous tasks are just normal calls to
normally registered browser views (or other traversable callables) and
they authenticated using PAS as all the other requests.

In addition, it's possible to configure views so that they are visible
only for asynchronous requests. Also, collective.taskqueue ships with a
special PAS-plugin, which authenticates each request as the user who
queued it.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing
%py_requires zope.configuration zope.testing z3c.form

%description tests
collective.taskqueue enables asynchronous tasks in Plone add-ons by
providing a small framework for asynchronously queueing requests to
ZPublisher. With this aproachasynchronous tasks are just normal calls to
normally registered browser views (or other traversable callables) and
they authenticated using PAS as all the other requests.

In addition, it's possible to configure views so that they are visible
only for asynchronous requests. Also, collective.taskqueue ships with a
special PAS-plugin, which authenticates each request as the user who
queued it.

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
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.dev0.git20150126
- Version 0.7.2.dev0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev0.git20141229
- Version 0.7.1.dev0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.dev0.git20141219
- Initial build for Sisyphus

