Name: python3-module-samsungtvws
Version: 1.4.0
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
It currently supports modern TVs with Ethernet or Wi-Fi connectivity.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/samsungtvws
%python3_sitelibdir/samsungtvws-%version-*-info

%changelog
* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- initial

