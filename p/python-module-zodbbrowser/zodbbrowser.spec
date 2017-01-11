%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zodbbrowser
%def_disable check

Name: python-module-%oname
Version: 0.13.0
#Release: alt2.dev0.git20150225
Summary: ZODB browser
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zodbbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mgedmin/zodbbrowser.git
Source0: https://pypi.python.org/packages/33/09/5dee00673388e7616e223423cbf5e9186310baceb67166ce3ed751411c11/%{oname}-%{version}.tar.gz

BuildRequires: python-module-coverage python-module-pytest python-module-zope.app.server python-module-zope.app.session python-module-zope.app.testing python-module-zope.testrunner

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-ZODB3 python-module-simplejson
#BuildPreReq: python-module-lxml python-module-cssselect
#BuildPreReq: python-module-unittest2 python-module-persistent
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-zope.app.pagetemplate
#BuildPreReq: python-module-zope.app.publication
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.location
#BuildPreReq: python-module-zope.publisher
#BuildPreReq: python-module-zope.security-tests
#BuildPreReq: python-module-zope.traversing-tests
#BuildPreReq: python-module-zope.cachedescriptors
#BuildPreReq: python-module-zope.app.container
#BuildPreReq: python-module-zope.app.testing
#BuildPreReq: python-module-zope.testbrowser
#BuildPreReq: python-module-zope.app.authentication
#BuildPreReq: python-module-zope.app.component
#BuildPreReq: python-module-zope.securitypolicy
#BuildPreReq: python-module-zope.app.server
#BuildPreReq: python-module-zope.app.session
#BuildPreReq: python-module-zope.app.zcmlfiles
#BuildPreReq: python-module-zope.server
#BuildPreReq: python-module-zope.error
#BuildPreReq: python-module-zope.exceptions
#BuildPreReq: python-module-zope.session
#BuildPreReq: python-module-zope.hookable
#BuildPreReq: python-module-RestrictedPython
#BuildPreReq: python-module-zope.testrunner
#BuildPreReq: python-module-zope.password-tests

%py_provides %oname
#%py_requires ZODB3 zope.app.pagetemplate zope.app.publication simplejson
#%py_requires zope.component zope.interface zope.location zope.publisher
#%py_requires zope.security zope.traversing zope.cachedescriptors
#%py_requires zope.app.container zope.app.authentication zope.app.server
#%py_requires zope.app.component zope.securitypolicy zope.app.session
#%py_requires zope.app.zcmlfiles zope.server zope.error zope.exceptions
#%py_requires zope.session zope.hookable RestrictedPython persistent

%description
The ZODB browser allows you to inspect persistent objects stored in the
ZODB, view their attributes and historical changes made to them.

WARNING:
ZODB is based on Python pickles, which are not secure - they allow
arbitrary command execution. Do not use zodbbrowser on databases from
untrusted sources.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.app.testing zope.testbrowser lxml cssselect unittest2
#%py_requires zope.testrunner zope.component.testing
#%py_requires zope.password.testing zope.traversing.testing
#%py_requires zope.security.testing

%description tests
The ZODB browser allows you to inspect persistent objects stored in the
ZODB, view their attributes and historical changes made to them.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
py.test -vv

%files
%doc *.txt *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*

%files tests
%python_sitelibdir/*/*test*

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1
- automated PyPI update

* Wed Jun 15 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.1-alt2.dev0.git20150225.1
- (AUTO) subst_x86_64.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.12.1-alt2.dev0.git20150225
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.dev0.git20150225
- Version 0.12.1.dev0

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.dev0.git20150213
- Initial build for Sisyphus

