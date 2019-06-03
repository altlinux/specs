%define oname asyncssh

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.17.0
Release: alt1

Summary: AsyncSSH: Asynchronous SSHv2 client and server library

License: Eclipse Public License v1.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncssh/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ronf/asyncssh.git
# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-intro

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-pycrypto
#BuildPreReq: python-module-cryptography python-module-curve25519
%py_provides %oname
%py_requires asyncio Crypto curve25519
%py_use cryptography >= 2.7
%endif
#BuildPreReq: %_bindir/openssl
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
%endif



%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio
framework.

%package -n python3-module-%oname
Summary: AsyncSSH: Asynchronous SSHv2 client and server library
Group: Development/Python3
%py3_provides %oname
%if_with python3
%py3_requires asyncio 
%py3_use Crypto curve25519
%py3_use cryptography >= 2.7
%endif

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

rm -f %buildroot%python_sitelibdir/%oname/*_win32*
rm -f %buildroot%python3_sitelibdir/%oname/*_win32*

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
%doc COPYRIGHT LICENSE README* examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc COPYRIGHT LICENSE README* examples
%python3_sitelibdir/*
%endif

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.0-alt1
- new version 1.17.0 (with rpmrb script)
- switch to build from tarball

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.2-alt1.git20150126.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20150126
- Version 0.9.2

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20141204
- Initial build for Sisyphus

