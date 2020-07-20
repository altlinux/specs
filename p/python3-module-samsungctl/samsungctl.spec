Name: python3-module-samsungctl
Version: 0.7.1
Release: alt1

Summary: Python library for remote controlling Samsung TV sets
License: MIT
Group: Development/Python
Url: https://pypi.org/project/voluptuous-serialize/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Python library for remote controlling Samsung TV sets via a TCP/IP connection.
It currently supports both pre-2016 TVs as well most of the modern Tizen-OS TVs
with Ethernet or Wi-Fi connectivity.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/samsungctl
%python3_sitelibdir/samsungctl-%version-*-info

%changelog
* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- initial
