%define oname asyncssh

%def_with check

Name: python3-module-%oname
Version: 2.14.2
Release: alt1

Summary: AsyncSSH: Asynchronous SSHv2 client and server library

License: Eclipse Public License v1.0
Group: Development/Python3
URL: https://pypi.org/project/asyncssh
VCS: https://github.com/ronf/asyncssh

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-intro

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-OpenSSL
BuildRequires: openssl
BuildRequires: openssh-clients
%endif

%py3_provides %oname
%py3_requires asyncio
%py3_use Crypto curve25519
%py3_use cryptography >= 2.7

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio
framework.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -v %buildroot%python3_sitelibdir/%oname/*_win32*

%check
%pyproject_run_unittest

%files
%doc COPYRIGHT LICENSE README* examples
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Jun 05 2024 Grigory Ustinov <grenka@altlinux.org> 2.14.2-alt1
- Build new version.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.17.0-alt2
- Drop python2 support.

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

