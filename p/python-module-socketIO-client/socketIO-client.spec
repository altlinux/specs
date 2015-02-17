%define oname socketIO-client

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt1.git20150216
Summary: A socket.io client library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/socketIO-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/invisibleroads/socketIO-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-six
BuildPreReq: python-module-websocket-client python-module-nose
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-six
BuildPreReq: python3-module-websocket-client python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides socketIO_client
%py_requires requests six websocket

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
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.git20150216
- Initial build for Sisyphus

