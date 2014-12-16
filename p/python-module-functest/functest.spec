%define oname functest
Name: python-module-%oname
Version: 0.8.8
Release: alt1
Summary: Functional test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/functest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildArch: noarch

%py_provides %oname

%description
Functest is a test tool/framework for testing in python.

It focuses on strong debugging, zero boiler plate, setup/teardown module
hierarchies, and distributed result reporting.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt1
- Initial build for Sisyphus

