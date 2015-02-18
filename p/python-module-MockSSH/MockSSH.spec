%define oname MockSSH

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt1.git20141214
Summary: Mock an SSH server and all commands it supports
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/MockSSH/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ncouture/MockSSH.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core python-module-twisted-conch
BuildPreReq: python-module-pycrypto python-module-paramiko
BuildPreReq: python-module-pyasn1 python-module-hy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core python3-module-twisted-conch
BuildPreReq: python3-module-pycrypto python3-module-paramiko
BuildPreReq: python3-module-pyasn1 python3-module-hy
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname mocksshy
%py_requires twisted.python twisted.conch Crypto paramiko pyasn1 hy

%description
MockSSH was developed to emulate operating systems behind SSH servers in
order to test task automation without having access to the real servers.

There has been interest in using MockSSH to perform end-to-end unit
tests against SSH servers and as such, a threaded version of MockSSH
server is available as of version 1.4 (thanks to Claudio Mignanti).

MockSSH is derived from kippo, an SSH honeypot.

%package -n python3-module-%oname
Summary: Mock an SSH server and all commands it supports
Group: Development/Python3
%py3_provides %oname mocksshy
%py3_requires twisted.python twisted.conch Crypto paramiko pyasn1 hy

%description -n python3-module-%oname
MockSSH was developed to emulate operating systems behind SSH servers in
order to test task automation without having access to the real servers.

There has been interest in using MockSSH to perform end-to-end unit
tests against SSH servers and as such, a threaded version of MockSSH
server is available as of version 1.4 (thanks to Claudio Mignanti).

MockSSH is derived from kippo, an SSH honeypot.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
	sed -i 's|#!/usr/bin/env hy|#!/usr/bin/env hy.py3|' $i
	2to3 -w -n $i ||:
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
%doc *.md examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.?y3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%_bindir/*.?y3
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.git20141214
- Initial build for Sisyphus

