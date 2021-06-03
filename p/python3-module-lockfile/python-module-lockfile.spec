%define oname lockfile

Name: python3-module-%oname
Version: 0.12.2
Release: alt2

Summary: A platform-independent file locking module

Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.python.org/packages/source/l/lockfile/lockfile-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc ACKS LICENSE README.rst RELEASE-NOTES doc/
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.2-alt2
- Drop python2 support.

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.12.2-alt1
- new version 0.12.2 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1
- Added module for Python 3

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Linux Sisyphus

* Thu Jul 23 2009 Silas Sewell <silas@sewell.ch> - 0.8-1
- Initial build.
