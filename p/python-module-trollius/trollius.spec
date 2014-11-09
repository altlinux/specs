%define oname trollius

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: Port of the Tulip project (asyncio module, PEP 3156) on Python 2
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/trollius/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-futures python-module-sphinx-devel
BuildPreReq: python-modules-wsgiref python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%add_python_req_skip msvcrt

%description
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Port of the Tulip project (asyncio module, PEP 3156) on Python 2
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip msvcrt

%description -n python3-module-%oname
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related
primitives.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc AUTHORS README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples doc/build/html

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

