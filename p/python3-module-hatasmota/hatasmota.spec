Name: python3-module-hatasmota
Version: 0.10.1
Release: alt1.1

Summary: Python library to interface with Tasmota devices
License: MIT
Group: Development/Python
Url: https://pypi.org/project/hatasmota
VCS: https://github.com/emontnemery/hatasmota

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/hatasmota
%python3_sitelibdir/hatasmota-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt1.1
- Demodernized packaging.

* Fri Oct 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.10.1-alt1
- 0.10.1 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.2-alt1
- 0.9.2 released

* Mon Jan 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt1
- 0.8.0 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt1
- 0.7.3 released

* Wed May 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.5-alt1
- 0.6.5 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.4-alt1
- 0.6.4 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.3-alt1
- 0.6.3 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.1-alt1
- 0.6.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Tue Jun 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt1
- 0.5.1 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.20-alt1
- 0.2.20

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.19-alt1
- 0.2.19

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.9-alt1
- initial
