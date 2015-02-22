%define mname ztfy
%define oname %mname.base
Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: ZTFY base content classes
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.schema

%py_provides %oname
%py_requires zope.component zope.i18nmessageid zope.interface ztfy.file
%py_requires ztfy.utils zope.intid zope.traversing zope.container
%py_requires zope.schema %mname

%description
A small set of generic content interfaces, adapters and base classes
associated to ZTFY packages.

Most of these have been extracted from ZTFY.blog to reduce dependencies
with this package from other application packages not really using
ZTFY.blog content management features.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
A small set of generic content interfaces, adapters and base classes
associated to ZTFY packages.

Most of these have been extracted from ZTFY.blog to reduce dependencies
with this package from other application packages not really using
ZTFY.blog content management features.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

