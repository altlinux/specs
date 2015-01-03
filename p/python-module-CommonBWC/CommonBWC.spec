%define oname CommonBWC
Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: A BlazeWeb component to hold libraries shared by other components and apps
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/CommonBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-PasteDeploy
BuildPreReq: python-module-BlazeForm python-module-BlazeWeb-tests

%py_provides commonbwc
%py_requires blazeweb blazeform

%description
CommonBWC is a component for BlazeWeb applications. It has views,
classes, and templates that are common for many web applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires blazeweb.testing

%description tests
CommonBWC is a component for BlazeWeb applications. It has views,
classes, and templates that are common for many web applications.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/lib/testing.*

%files tests
%python_sitelibdir/*/lib/testing.*

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

