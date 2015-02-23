%define mname ztfy
%define oname %mname.zmq
Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: ZTFY integration of ZeroMQ library
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.zmq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zmq
BuildPreReq: python-modules-multiprocessing
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname zmq zope.i18nmessageid zope.interface

%description
ZTFY.zmq is a small ZTFY integration of ZeroMQ library.

It provides two main classes which are:

* ZMQProcess, which is a ZMQ listening process, based on multiprocessing
  package.
* ZMQMessageHandler, which is a simple ZMQ messages handler which
  delegates it's functionality to a ZMQ agnostic handling class.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ZTFY.zmq is a small ZTFY integration of ZeroMQ library.

This packgae contains tests for %oname.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

