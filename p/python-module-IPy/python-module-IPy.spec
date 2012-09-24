%define mname IPy
Name: python-module-%mname
Version: 0.75
Release: alt1
Summary: Python module for handling IPv4 and IPv6 Addresses and Networks
URL: https://github.com/haypo/python-ipy
Source: %mname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks in
a fashion similar to perl's Net::IP and friends. The IP class allows
a comfortable parsing and handling for most notations in use for IPv4 and IPv6
Addresses and Networks.


%prep
%setup -q -n %mname-%version


%build
%__python setup.py build


%install
%__python setup.py install --skip-build --root %buildroot --compile


%check
%__python test/test_IPy.py


%files
%doc AUTHORS ChangeLog README
%python_sitelibdir_noarch/*


%changelog
* Mon Sep 24 2012 Led <led@altlinux.ru> 0.75-alt1
- initial build for ALTLinux
