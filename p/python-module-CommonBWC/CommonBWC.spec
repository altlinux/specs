%define _unpackaged_files_terminate_build 1
%define oname CommonBWC
Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: A BlazeWeb component to hold libraries shared by other components and apps
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/CommonBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/58/c8/608573890a8ce47bd9d32b4b144cc51d1f59669e0cb1a1bfe4b52332ea36/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-PasteDeploy
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
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/lib/testing.*

%files tests
%python_sitelibdir/*/lib/testing.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

