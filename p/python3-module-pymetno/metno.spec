Name: python3-module-pymetno
Version: 0.13.0
Release: alt1.1

Provides: python3-module-metno = %EVR
Obsoletes: python3-module-metno

Summary: Python library to talk to the met.no api
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyMetno
VCS: https://github.com/Danielhiversen/pyMetno

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
%doc LICENSE README.*
%python3_sitelibdir/metno
%python3_sitelibdir/pymetno-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt1.1
- Demodernized packaging.

* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.13.0-alt1
- 0.13.0 released

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt1
- 0.12.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- 0.10.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- 0.9.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt1
- 0.8.3 released

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- 0.8.2 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
