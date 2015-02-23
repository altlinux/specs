%define mname ztfy
%define oname %mname.appskin

Name: python-module-%oname
Version: 0.3.7
Release: alt1
Summary: ZTFY application base skin
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.appskin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ztfy.bootstrap
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname zope.component zope.i18nmessageid zope.interface
%py_requires ztfy.bootstrap ztfy.i18n ztfy.skin ztfy.utils ztfy.file
%py_requires fanstatic

%description
ZTFY.appskin is a base skin for ZTFY based applications.

It includes a responsive design based on Twitter Bootstrap.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.appskin is a base skin for ZTFY based applications.

It includes a responsive design based on Twitter Bootstrap.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

