%define oname AuthBWC

%def_disable check

Name: python-module-%oname
Version: 0.2.3
Release: alt1
Summary: A user authentication and authorization component for the BlazeWeb framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/AuthBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-PasteDeploy
BuildPreReq: python-module-webtest python-module-pyquery
BuildPreReq: python-module-CommonBWC python-module-BlazeWeb-tests
BuildPreReq: python-module-SQLAlchemyBWC python-module-TemplatingBWC
#BuildPreReq: python-module-WebGrid python-module-BaseBWA

%py_provides authbwc
%py_requires blazeweb commonbwc sqlalchemybwc
%add_python_req_skip basebwa webgrid

%description
AuthBWC is a component for BlazeWeb applications. It provides users,
groups, permissions, related helpers and views. Proper integration of
this component will allow applications to have views that can only be
accessed by certain users.

Includes email notifications when an account is created as well as an
email based password reset mechanism.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires webtest

%description tests
AuthBWC is a component for BlazeWeb applications. It provides users,
groups, permissions, related helpers and views. Proper integration of
this component will allow applications to have views that can only be
accessed by certain users.

Includes email notifications when an account is created as well as an
email based password reset mechanism.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR authbwc_ta %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus

