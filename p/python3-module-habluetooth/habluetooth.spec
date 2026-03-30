%def_with check

Name: python3-module-habluetooth
Version: 5.8.0
Release: alt1.1

Summary: High availability Bluetooth
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/habluetooth
VCS: https://github.com/bluetooth-devices/habluetooth

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-poetry-core
BuildRequires: python3-module-cython

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-codspeed
BuildRequires: python3-module-async-interrupt
BuildRequires: python3-module-bleak
BuildRequires: python3-module-bleak-retry-connector
BuildRequires: python3-module-bluetooth-data-tools
BuildRequires: python3-module-btsocket
BuildRequires: python3-module-bluetooth-auto-recovery
BuildRequires: python3-module-freezegun
%endif

#%%python3_set_limited_api 3.12

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/habluetooth
%python3_sitelibdir/habluetooth-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.8.0-alt1.1
- Demodernized packaging.

* Fri Dec 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 5.8.0-alt1
- 5.8.0 released

* Fri Oct 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 5.7.0-alt1
- 5.7.0 released

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 5.6.2-alt1
- 5.3.1 -> 5.6.2.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- 5.3.0 -> 5.3.1.

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 3.8.0 -> 5.3.0.

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.8.0-alt1
- 3.8.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.0-alt1
- 3.6.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.0-alt1
- 3.4.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.3-alt1
- 3.1.3 released

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.1-alt1
- 2.8.1 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.0-alt1
- 2.8.0 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.2-alt1
- 2.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released
