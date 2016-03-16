%define oname websocket-client

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.32.0
Release: alt1.1.1
Summary: WebSocket client for python. hybi13 is supported
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/websocket-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/liris/websocket-client.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-backports.ssl_match_hostname
#BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six
%endif

%py_provides websocket
%py_requires backports.ssl_match_hostname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: WebSocket client for python. hybi13 is supported
Group: Development/Python3
%py3_provides websocket

%description -n python3-module-%oname
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
websocket-client module is WebSocket client for python. This provide the
low level APIs for WebSocket. All APIs are the synchronous functions.

websocket-client supports only hybi-13.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.32.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.32.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.org> 0.32.0-alt1
- new version

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.git20141211
- Initial build for Sisyphus

