%define oname lockfile

Name: python-module-%oname
Version: 0.8
Release: alt1.1

Summary: A platform-independent file locking module

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://smontanaro.dyndns.org/python/%oname-%version.tar

BuildArch: noarch

BuildRequires: python-devel

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
%python_build

%install
%python_install

%files
%doc ACKS LICENSE README RELEASE-NOTES doc/
%python_sitelibdir/%oname.py*
%python_sitelibdir/%oname-%version-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Linux Sisyphus

* Thu Jul 23 2009 Silas Sewell <silas@sewell.ch> - 0.8-1
- Initial build.
