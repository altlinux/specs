%define oname netifaces

%def_with python3

Name: python-module-%oname
Version: 0.10.6
Release: alt1.1

%setup_python_module %oname

Summary: Portable network interface information

License: MIT License
Group: Development/Python
Url: http://alastairs-place.net/netifaces

#Source: http://alastairs-place.net/projects/netifaces/netifaces-%version.tar
# Source-url: https://pypi.io/packages/source/n/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux
and Solaris.  On Windows, it is currently not able to retrieve IPv6
addresses, owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement
either getifaddrs() or support the SIOCGIFxxx socket options, although the
data provided by the socket options is normally less complete.

%package -n python3-module-%oname
Summary: Portable network interface information
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux
and Solaris.  On Windows, it is currently not able to retrieve IPv6
addresses, owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement
either getifaddrs() or support the SIOCGIFxxx socket options, although the
data provided by the socket options is normally less complete.

%prep
%setup

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
%doc README.rst
%python_sitelibdir/%modulename-*.egg-info
%python_sitelibdir/%modulename.so

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/%modulename-*.egg-info
%python3_sitelibdir/%modulename.*.so
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.6-alt1
- new version (0.10.6) with rpmgs script

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.4-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.4-alt1
- Version 0.10.4
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- new version 0.8 (with rpmrb script)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 22 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
