%define _unpackaged_files_terminate_build 1
%define oname nazca
Name: python-module-%oname
Version: 0.7.2
Release: alt1
Summary: Python library for data alignment
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/nazca/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/f9/5a/92d007b82a5fb40a8b0697b2b89aad1a1cb506b0d736660b34406e7e54eb/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

