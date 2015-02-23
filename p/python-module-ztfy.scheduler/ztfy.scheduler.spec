%define mname ztfy
%define oname %mname.scheduler
Name: python-module-%oname
Version: 0.5.2
Release: alt1
Summary: ZTFY scheduler package for ZTK/ZopeApp
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.scheduler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-apscheduler python-module-paramiko
BuildPreReq: python-module-transaction python-module-ZEO
BuildPreReq: python-module-lovely.memcached
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zc.catalog
BuildPreReq: python-module-zc.lockfile
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.generations
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.mail
BuildPreReq: python-module-ztfy.security
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.zmi
BuildPreReq: python-module-ztfy.zmq
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname apscheduler lovely.memcached paramiko transaction
%py_requires z3c.form z3c.formjs z3c.language.switch z3c.table zope.i18n
%py_requires z3c.template zc.catalog zc.lockfile zope.app.publication
%py_requires zope.authentication zope.component zope.container zope.site
%py_requires zope.dublincore zope.event zope.generations zope.interface
%py_requires zope.i18nmessageid zope.intid zope.location zope.schema
%py_requires zope.processlifetime zope.security zope.sendmail ztfy.i18n
%py_requires zope.traversing ztfy.jqueryui ztfy.mail ztfy.security
%py_requires ztfy.skin ztfy.utils ztfy.zmi ztfy.zmq ZEO

%description
ztfy.scheduler is a base package for those which need to build scheduled
tasks which can run inside a ZTK/ZopeApp based environment (ZEO is
required !). These tasks can be scheduled:

* on a cron-style base,
* at a given date/time (like the "at" command)
* or at a given interval.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.scheduler is a base package for those which need to build scheduled
tasks which can run inside a ZTK/ZopeApp based environment (ZEO is
required !). These tasks can be scheduled:

* on a cron-style base,
* at a given date/time (like the "at" command)
* or at a given interval.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

