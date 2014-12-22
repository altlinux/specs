%define mname collective
%define oname %mname.azipfele
Name: python-module-%oname
Version: 1.1.3
Release: alt1.dev0.git20141219
Summary: Creates Zip files from Plone or other content asynchronous
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.azipfele/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.azipfele.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-memcached
BuildPreReq: python-module-interlude python-module-ipdb
BuildPreReq: python-module-openid
BuildPreReq: python-module-collective.zamqp
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.contenttypes-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.zamqp Plone plone.api memcache plone.uuid
%py_requires plone.app.contenttypes plone.folder plone.dexterity
%py_requires plone.namedfile plone.app.textfield plone.app.uuid
%py_requires zope.publisher zope.interface zope.component zope.event
%py_requires zope.i18nmessageid

%description
This is a basic module aiming to create ZIP files asynchronous. Even if
it has some basic built in data-extractors, it is not meant as a
out-of-the-box package, but for integrators and addon-product authors.

Creating ZIP files in a request-response cycle may take a lot of time.
With this package a zip job info is queued into a AMQP-Server (such as
RabbitMQ).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing
%py_requires plone.app.contenttypes.testing

%description tests
This is a basic module aiming to create ZIP files asynchronous. Even if
it has some basic built in data-extractors, it is not meant as a
out-of-the-box package, but for integrators and addon-product authors.

Creating ZIP files in a request-response cycle may take a lot of time.
With this package a zip job info is queued into a AMQP-Server (such as
RabbitMQ).

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
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141219
- Initial build for Sisyphus

