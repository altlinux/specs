%define oname websockets

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 2.3
Release: alt1.git20141103.1
Summary: An implementation of the WebSocket Protocol (RFC 6455)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/websockets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aaugustin/websockets.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-setuptools-tests rpm-build-python3

%description
websockets is a library for developing WebSocket servers and clients in
Python. It implements RFC 6455 with a focus on correctness and
simplicity. It passes the Autobahn Testsuite.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
websockets is a library for developing WebSocket servers and clients in
Python. It implements RFC 6455 with a focus on correctness and
simplicity. It passes the Autobahn Testsuite.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An implementation of the WebSocket Protocol (RFC 6455)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
websockets is a library for developing WebSocket servers and clients in
Python. It implements RFC 6455 with a focus on correctness and
simplicity. It passes the Autobahn Testsuite.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
websockets is a library for developing WebSocket servers and clients in
Python. It implements RFC 6455 with a focus on correctness and
simplicity. It passes the Autobahn Testsuite.

Built on top on Python's asynchronous I/O support introduced in PEP
3156, it provides an API based on coroutines, making it easy to write
highly concurrent applications.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst example compliance
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst example compliance
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3-alt1.git20141103.1
- NMU: Use buildreq for BR.

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.git20141103
- Initial build for Sisyphus

