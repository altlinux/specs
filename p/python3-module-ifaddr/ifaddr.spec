Name: python3-module-ifaddr
Version: 0.1.6
Release: alt1

Summary: Python library to enumerate own IP addressess
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ifaddr/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Enumerates all IP addresses on all network adapters of the system

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/ifaddr
%python3_sitelibdir/ifaddr-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.6-alt1
- initial
