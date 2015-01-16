%define oname nazca
Name: python-module-%oname
Version: 0.7.1
Release: alt1
Summary: Python library for data alignment
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/nazca/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-lxml
BuildPreReq: python-module-scipy python-module-scikit-learn
BuildPreReq: python-module-dateutil

%py_provides %oname
%py_requires scipy sklearn lxml dateutil

%description
Python library for data alignment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python library for data alignment.

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
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/examples

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

