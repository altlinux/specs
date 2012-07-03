%define version 0.6
%define release alt1
%setup_python_module netifaces

Summary: Portable network interface information
Name: python-module-netifaces
Version: 0.6
Release: %release.1

Source: %modulename-%version.tar.gz
License: MIT License
Group: Development/Python
Url: http://alastairs-place.net/netifaces

BuildRequires: python-devel python-module-setuptools

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

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/%modulename-*.egg-info
%python_sitelibdir/%modulename.so

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 22 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
