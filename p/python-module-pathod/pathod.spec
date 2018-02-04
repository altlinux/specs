%define oname pathod
Name: python-module-%oname
Version: 0.11
Release: alt1.git20141111.1
Summary: A pathological HTTP/S daemon for testing and stressing clients
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pathod/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitmproxy/pathod.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-netlib
BuildPreReq: python-module-chardet
BuildPreReq: python-module-pip python-module-requests
BuildPreReq: python-module-flask python-module-mock
BuildPreReq: python-module-nose python-module-nose-cov
BuildPreReq: python-module-coveralls python-module-passlib

%py_provides libpathod

%description
pathod is a collection of pathological tools for testing and torturing
HTTP clients and servers. The project has three components:

* pathod, an pathological HTTP daemon.
* pathoc, a perverse HTTP client.
* libpathod.test, an API for easily using pathod and pathoc in unit
  tests.

%package test
Summary: Test for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip pathod

%description test
pathod is a collection of pathological tools for testing and torturing
HTTP clients and servers. The project has three components:

* pathod, an pathological HTTP daemon.
* pathoc, a perverse HTTP client.
* libpathod.test, an API for easily using pathod and pathoc in unit
  tests.

This package contains test for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=$PWD
python setup.py test
#py.test

%files
%doc CHANGELOG README.* examples
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files test
%python_sitelibdir/*/test.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11-alt1.git20141111.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20141111
- Initial build for Sisyphus

