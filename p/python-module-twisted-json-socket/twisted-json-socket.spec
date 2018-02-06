%define oname twisted-json-socket

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20141113.1.1.1
Summary: Protocol for twisted json socket
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/twisted-json-socket/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/madssj/twisted-json-socket.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-twisted-core python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-twisted-core python-tools-2to3
%endif

%py_provides twistedjsonsocket
%py_requires twisted.python json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-twisted-core python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pycparser python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-setuptools python-module-twisted-logger python3-module-cryptography python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-zope rpm-build-python3 time

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.git20141113.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20141113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20141113.1
- NMU: Use buildreq for BR.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141113
- Version 0.1.3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20141112
- Initial build for Sisyphus

