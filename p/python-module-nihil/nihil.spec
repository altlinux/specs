%define oname nihil

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141209
Summary: Nothing-but-Iffy HTTP I/O Library
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/nihil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aperezdc/nihil.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-Trololio
BuildPreReq: python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-Trololio
BuildPreReq: python3-module-unittest2
%endif

%py_provides %oname
%py_requires six trololio

%description
NIHIL is a small package which contains utilities to make HTTP services
using the Python asyncio framework. It provides the following
facilities:

* Request and Response objects (ala WebOb, but simpler).
* HTTP protocol implementation for asyncio.
* HTTP request parser.
* Request routing.

NIHIL lends itself to be used as a small web framework, by means of the
routing system; or to use the lower level components its parts for other
purposes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires unittest2

%description tests
NIHIL is a small package which contains utilities to make HTTP services
using the Python asyncio framework. It provides the following
facilities:

* Request and Response objects (ala WebOb, but simpler).
* HTTP protocol implementation for asyncio.
* HTTP request parser.
* Request routing.

NIHIL lends itself to be used as a small web framework, by means of the
routing system; or to use the lower level components its parts for other
purposes.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Nothing-but-Iffy HTTP I/O Library
Group: Development/Python3
%py3_provides %oname
%py3_requires six trololio

%description -n python3-module-%oname
NIHIL is a small package which contains utilities to make HTTP services
using the Python asyncio framework. It provides the following
facilities:

* Request and Response objects (ala WebOb, but simpler).
* HTTP protocol implementation for asyncio.
* HTTP request parser.
* Request routing.

NIHIL lends itself to be used as a small web framework, by means of the
routing system; or to use the lower level components its parts for other
purposes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires unittest2

%description -n python3-module-%oname-tests
NIHIL is a small package which contains utilities to make HTTP services
using the Python asyncio framework. It provides the following
facilities:

* Request and Response objects (ala WebOb, but simpler).
* HTTP protocol implementation for asyncio.
* HTTP request parser.
* Request routing.

NIHIL lends itself to be used as a small web framework, by means of the
routing system; or to use the lower level components its parts for other
purposes.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -p -m644 %oname/META %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname/META %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst doc/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141209
- Initial build for Sisyphus

