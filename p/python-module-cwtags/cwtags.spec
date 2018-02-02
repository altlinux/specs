%define oname cwtags
Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: A small convenience html tags lib for CubicWeb
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/cwtags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

%py_provides %oname
Requires: cubicweb

%description
A small convenience html tags lib for CubicWeb.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A small convenience html tags lib for CubicWeb.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python test/unittest_tags.py

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

