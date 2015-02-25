%define mname ztfy
%define oname %mname.beaker
Name: python-module-%oname
Version: 0.1.0
Release: alt1
Summary: Beaker package integration for ZTFY
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.beaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-beaker
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ztfy.baseskin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.minmax
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.session
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.componentvocabulary

%py_provides %oname
%py_requires %mname beaker zope.component zope.i18nmessageid ztfy.utils
%py_requires zope.interface ztfy.baseskin zope.schema zope.minmax
%py_requires zope.container zope.session zope.configuration
%py_requires zope.componentvocabulary

%description
ZTFY.beaker is a small wrapper around Beaker session and caching
library.

It allows you to define a Beaker session throught a ZCML configuration
directive to include it in a WSGI application based on ZTFY packages.

A BeakerSessionUtility can then be created and registered to act as a
session data container.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.beaker is a small wrapper around Beaker session and caching
library.

It allows you to define a Beaker session throught a ZCML configuration
directive to include it in a WSGI application based on ZTFY packages.

A BeakerSessionUtility can then be created and registered to act as a
session data container.

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
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

