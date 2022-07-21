Name: python3-module-ifaddr
Version: 0.2.0
Release: alt1

Summary: Python library to enumerate own IP addressess
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ifaddr/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Enumerates all IP addresses on all network adapters of the system

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/ifaddr
%python3_sitelibdir/ifaddr-%version.dist-info

%changelog
* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.7-alt1
- 0.1.7 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.6-alt1
- initial
