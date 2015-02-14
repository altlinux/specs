%define mname gocept
%define oname %mname.amqprun
Name: python-module-%oname
Version: 0.15.1
Release: alt1
Summary: Helps you writing and running AMQP consumers, and sending AMQP messages
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.amqprun/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-mock
BuildPreReq: python-module-zconfig python-module-oldpika
BuildPreReq: python-module-transaction python-module-amqplib
BuildPreReq: python-module-tcpwatch python-module-nose
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.xmlpickle
BuildPreReq: python-module-gocept.filestore
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-gocept.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname ZConfig oldpika transaction zope.component zope.event
%py_requires zope.configuration zope.interface zope.schema
%py_requires zope.xmlpickle gocept.filestore zope.security

%description
gocept.amqprun helps you writing and running AMQP consumers, and sending
AMQP messages. It currently only supports AMQP 0-8 and integrates with
the Zope Tool Kit (ZTK) so you can use adapters, utilities and all the
buzz.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires amqplib gocept.testing mock plone.testing tcpwatch
%py_requires zope.testing

%description tests
gocept.amqprun helps you writing and running AMQP consumers, and sending
AMQP messages. It currently only supports AMQP 0-8 and integrates with
the Zope Tool Kit (ZTK) so you can use adapters, utilities and all the
buzz.

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
#nosetests -v

%files
%doc *.txt example.* recv.py send.py
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1
- Initial build for Sisyphus

