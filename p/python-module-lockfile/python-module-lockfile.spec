%define oname lockfile

%def_with python3

Name: python-module-%oname
Version: 0.11.0
Release: alt1

Summary: A platform-independent file locking module

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.python.org/packages/source/l/lockfile/lockfile-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-module-distribute python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pbr
%endif

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%package -n python3-module-%oname
Summary: A platform-independent file locking module
Group: Development/Python3

%description -n python3-module-%oname
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ACKS LICENSE README.rst RELEASE-NOTES doc/
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc ACKS LICENSE README.rst RELEASE-NOTES doc/
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-*.egg-info
%endif

%changelog
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
