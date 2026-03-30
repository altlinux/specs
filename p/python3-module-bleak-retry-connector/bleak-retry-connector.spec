%def_with check

Name: python3-module-bleak-retry-connector
Version: 4.5.0
Release: alt1.1

Summary: A connector for Bleak Client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak-retry-connector
VCS: https://github.com/bluetooth-devices/bleak-retry-connector

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-bleak
BuildRequires: python3-module-bluetooth-adapters
%endif

%description
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/bleak_retry_connector
%python3_sitelibdir/bleak_retry_connector-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1.1
- Demodernized packaging.

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.5.0-alt1
- 4.5.0 released

* Mon Dec 08 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.4.4-alt1
- 4.4.4 released

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1
- 3.6.0 -> 4.4.3.

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.0-alt1
- 3.6.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.0-alt1
- 3.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- 3.4.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt1
- 3.3.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.3-alt1
- 3.1.3 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13.0-alt1
- 2.13.0 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.2-alt1
- 2.8.2 released
