%define oname twisted-json-socket

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20141113
Summary: Protocol for twisted json socket
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/twisted-json-socket/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/madssj/twisted-json-socket.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core python-tools-2to3
%endif

%py_provides twistedjsonsocket
%py_requires twisted.python json

%description
Handles all connections to clients. Clienthandler maintains connections
with client and defines the client protocol.

To implement the protocol override connectionMade, connectionLost and
lineReceived.

%package -n python3-module-%oname
Summary: Protocol for twisted json socket
Group: Development/Python3
%py3_provides twistedjsonsocket
%py3_requires twisted.python

%description -n python3-module-%oname
Handles all connections to clients. Clienthandler maintains connections
with client and defines the client protocol.

To implement the protocol override connectionMade, connectionLost and
lineReceived.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3/tests -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141113
- Version 0.1.3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141112
- Initial build for Sisyphus

