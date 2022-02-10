Name: python3-module-hatasmota
Version: 0.3.1
Release: alt1

Summary: Python library to interface with Tasmota devices
License: MIT
Group: Development/Python
Url: https://pypi.org/project/hatasmota/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/hatasmota
%python3_sitelibdir/HATasmota-%version-*-info

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.20-alt1
- 0.2.20

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.19-alt1
- 0.2.19

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.9-alt1
- initial
