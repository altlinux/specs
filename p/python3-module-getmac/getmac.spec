Name: python3-module-getmac
Version: 0.9.4
Release: alt1

Summary: Python library to get the MAC address
License: MIT
Group: Development/Python
Url: https://pypi.org/project/getmac/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Pure-Python package to get the MAC address of network interfaces and hosts
on the local network.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/getmac
%python3_sitelibdir/getmac-%version.dist-info

%changelog
* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.4-alt1
- 0.9.4 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.3-alt1
- 0.9.3 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt1
- 0.8.3 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- initial
