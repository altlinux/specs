%define oname twisted-json-socket

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: Protocol for twisted json socket
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/twisted-json-socket/
BuildArch: noarch

# https://bitbucket.org/madssj/twisted-json-socket.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides twistedjsonsocket
%py3_requires twisted.python json

BuildRequires: python3-module-cryptography python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-zope python-tools-2to3


%description
Handles all connections to clients. Clienthandler maintains connections
with client and defines the client protocol.

To implement the protocol override connectionMade, connectionLost and
lineReceived.

%prep
%setup

find ./tests -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc README
%python3_sitelibdir/*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- python2 disabled

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

