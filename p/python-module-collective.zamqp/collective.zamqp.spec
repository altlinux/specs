%define mname collective
%define oname %mname.zamqp
Name: python-module-%oname
Version: 0.15.0
Release: alt1.dev0.git20141111
Summary: Asynchronous AMQP-integration for Plone (and Zope2)
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.zamqp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.zamqp.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.unconfigure python-module-transaction
BuildPreReq: python-module-pika python-module-testfixtures
BuildPreReq: python-module-rabbitfixture python-module-msgpack
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-grokcore.component
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-sauna.reload

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname z3c.unconfigure ZODB3 transaction zope.interface
%py_requires zope.component zope.publisher zope.event grokcore.component
%py_requires zope.processlifetime pika zope.deprecation sauna.reload

%description
collective.zamqp acts as a Zope Server by co-opting Zope's asyncore
mainloop (using asyncore-supporting AMQP-library pika), and injecting
consumed messages as requests to be handled by ZPublisher (exactly like
Zope ClockServer).

Therefore AMQP-messages are handled (by default) in a similar
environment to regular HTTP-requests: ZCA-hooks, events and everything
else behaving normally.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing zope.configuration

%description tests
collective.zamqp acts as a Zope Server by co-opting Zope's asyncore
mainloop (using asyncore-supporting AMQP-library pika), and injecting
consumed messages as requests to be handled by ZPublisher (exactly like
Zope ClockServer).

Therefore AMQP-messages are handled (by default) in a similar
environment to regular HTTP-requests: ZCA-hooks, events and everything
else behaving normally.

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
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.dev0.git20141111
- Initial build for Sisyphus

