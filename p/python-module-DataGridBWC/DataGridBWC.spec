%define oname DataGridBWC

%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: A BlazeWeb component for turning SQLAlchemy recordsets into HTML tables
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/DataGridBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-nose
BuildPreReq: python-module-mock python-module-xlwt
BuildPreReq: python-module-xlrd python-module-webtest
BuildPreReq: python-module-BlazeUtils python-module-BlazeWeb-tests
BuildPreReq: python-module-SQLAlchemyBWC python-module-dateutil
BuildPreReq: python-module-PasteDeploy
#BuildPreReq: python-module-WebGrid

%py_provides datagridbwc
%add_python_req_skip webgrid

%description
A BlazeWeb component for turning SQLAlchemy recordsets into HTML tables.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A BlazeWeb component for turning SQLAlchemy recordsets into HTML tables.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR datagridbwc_ta %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

