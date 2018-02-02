# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20130514.1.1
%define mname lovely
%define oname %mname.memcached
Name: python-module-%oname
Version: 0.2.2
#Release: alt1.git20130514
Summary: A memcached client utiltiy for zope 3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/lovely.memcached/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lovelysystems/lovely.memcached.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-memcached
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-z3c.configurator
BuildPreReq: python-module-zope.keyreference-tests
BuildPreReq: python-module-zope.securitypolicy
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.testbrowser
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.password-tests
BuildPreReq: python-module-zope.traversing-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires memcache zope.site zope.intid zope.event zope.interface
%py_requires zope.lifecycleevent zope.schema zope.security

%description
This package provides a zope3 utility that abstracts a client for
memcached servers see: http://www.danga.com/memcached.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires z3c.configurator zope.keyreference.testing
%py_requires zope.app.testing zope.testbrowser zope.securitypolicy
%py_requires zope.component.testing zope.password.testing
%py_requires zope.traversing.testing

%description tests
This package provides a zope3 utility that abstracts a client for
memcached servers see: http://www.danga.com/memcached.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.git20130514.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20130514.1
- (AUTO) subst_x86_64.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20130514
- Initial build for Sisyphus

