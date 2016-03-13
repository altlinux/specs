%define oname asyncssh

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.2
Release: alt1.git20150126.1.1
Summary: AsyncSSH: Asynchronous SSHv2 client and server library
License: Eclipse Public License v1.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncssh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ronf/asyncssh.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-pycrypto
#BuildPreReq: python-module-cryptography python-module-curve25519
%endif
#BuildPreReq: %_bindir/openssl
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-pycrypto
#BuildPreReq: python3-module-cryptography python3-module-curve25519
%endif

%py_provides %oname
%py_requires asyncio Crypto cryptography curve25519

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pycparser python3-module-setuptools
BuildRequires: python3-module-cryptography python3-module-curve25519 python3-module-pycrypto python3-module-pytest rpm-build-python3

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio
framework.

%package -n python3-module-%oname
Summary: AsyncSSH: Asynchronous SSHv2 client and server library
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio Crypto cryptography curve25519

%description -n python3-module-%oname
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio
framework.

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
%doc COPYRIGHT LICENSE README* docs/*.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc COPYRIGHT LICENSE README* docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20150126
- Version 0.9.2

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20141204
- Initial build for Sisyphus

