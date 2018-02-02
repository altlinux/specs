%define oname netlib

%def_disable check

Name: python-module-%oname
Version: 0.11.2
Release: alt1.git20141228.1
Summary: A collection of network utilities used by pathod and mitmproxy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/netlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitmproxy/netlib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: libssl-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pyasn1 python-module-OpenSSL
BuildPreReq: python-module-passlib python-module-mock
BuildPreReq: python-module-nose python-module-nose-cov
BuildPreReq: python-module-coveralls
#BuildPreReq: python-module-pathod

%py_provides %oname
%py_requires OpenSSL

%description
Netlib is a collection of network utility classes, used by the pathod
and mitmproxy projects. It differs from other projects in some
fundamental respects, because both pathod and mitmproxy often need to
violate standards. This means that protocols are implemented as small,
well-contained and flexible functions, and are designed to allow
misbehaviour when needed.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Netlib is a collection of network utility classes, used by the pathod
and mitmproxy projects. It differs from other projects in some
fundamental respects, because both pathod and mitmproxy often need to
violate standards. This means that protocols are implemented as small,
well-contained and flexible functions, and are designed to allow
misbehaviour when needed.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=$PWD
python setup.py test
py.test

%files
%doc *.mkd
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1.git20141228.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20141228
- Version 0.11.2

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.git20141115
- Version 0.11.1

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20141111
- Initial build for Sisyphus

