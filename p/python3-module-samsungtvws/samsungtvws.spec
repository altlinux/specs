Name: python3-module-samsungtvws
Version: 2.6.0
Release: alt1

Summary: Python library for remote controlling Samsung TV sets
License: MIT
Group: Development/Python
Url: https://pypi.org/project/voluptuous-serialize/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Python library for remote controlling Samsung TV sets via a TCP/IP connection.
It currently supports modern TVs with Ethernet or Wi-Fi connectivity.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/samsungtvws
%python3_sitelibdir/samsungtvws-%version.dist-info

%changelog
* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- initial

