%define oname TemplatingBWC
Name: python-module-%oname
Version: 0.3.1
Release: alt1.1
Summary: A BlazeWeb component with template themes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/TemplatingBWC/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-BlazeForm
BuildPreReq: python-module-BlazeWeb-tests python-module-PasteDeploy
BuildPreReq: python-module-CommonBWC python-module-DataGridBWC

%py_provides templatingbwc

%description
TemplatingBWC is a component for BlazeWeb applications. Its main purpose
is to provide a customizable yet generic template appropriate for
back-end, control-panel, or similiar use-oriented web applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
TemplatingBWC is a component for BlazeWeb applications. Its main purpose
is to provide a customizable yet generic template appropriate for
back-end, control-panel, or similiar use-oriented web applications.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

cp -fR templatingbwc_ta %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

