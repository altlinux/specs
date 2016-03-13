%define oname socketIO-client

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt1.git20150216.1.1
Summary: A socket.io client library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/socketIO-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/invisibleroads/socketIO-client.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-six
#BuildPreReq: python-module-websocket-client python-module-nose
#BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-six
#BuildPreReq: python3-module-websocket-client python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%py_provides socketIO_client
%py_requires requests six websocket

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3
BuildRequires: python-module-coverage python-module-nose python-module-requests python-module-setuptools-tests python-module-websocket-client python3-module-coverage python3-module-nose python3-module-requests python3-module-setuptools-tests python3-module-websocket-client rpm-build-python3

%description
Here is a socket.io client library for Python. You can use it to write
test code for your socket.io server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Here is a socket.io client library for Python. You can use it to write
test code for your socket.io server.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A socket.io client library
Group: Development/Python3
%py3_provides socketIO_client
%py3_requires requests six websocket

%description -n python3-module-%oname
Here is a socket.io client library for Python. You can use it to write
test code for your socket.io server.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Here is a socket.io client library for Python. You can use it to write
test code for your socket.io server.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *.goals
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.goals
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt1.git20150216.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1.git20150216.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.git20150216
- Initial build for Sisyphus

