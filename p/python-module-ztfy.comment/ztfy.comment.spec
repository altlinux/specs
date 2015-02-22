%define mname ztfy
%define oname %mname.comment
Name: python-module-%oname
Version: 0.3.3
Release: alt1
Summary: ZTFY comment package
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.comment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-ztfy.security
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner

%py_provides %oname
%py_requires %mname z3c.template zope.annotation zope.component
%py_requires zope.dublincore zope.event zope.i18n zope.interface
%py_requires zope.lifecycleevent zope.publisher zope.schema ztfy.skin
%py_requires zope.security ztfy.security ztfy.utils

%description
ZTFY comment package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
ZTFY comment package.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

