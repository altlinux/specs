%def_with check

Name: python3-module-aioesphomeapi
Version: 44.0.0
Release: alt1.1

Summary: Python API to ESPHome devices
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aioesphomeapi
VCS: https://github.com/esphome/aioesphomeapi

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cython

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-codspeed
BuildRequires: python3-module-protobuf
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-aiohappyeyeballs
BuildRequires: python3-module-async-interrupt
BuildRequires: python3-module-chacha20poly1305-reuseable
BuildRequires: python3-module-noiseprotocol
BuildRequires: python3-module-tzlocal
BuildRequires: python3-module-zeroconf
%endif

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
%_bindir/aioesphomeapi-*
%python3_sitelibdir/aioesphomeapi
%python3_sitelibdir/aioesphomeapi-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 44.0.0-alt1.1
- Demodernized packaging.

* Wed Feb 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 44.0.0-alt1
- 44.0.0 released

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 30.1.0-alt1
- 27.0.1 -> 30.1.0.

* Tue Nov 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 27.0.1-alt1
- 27.0.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 25.3.2-alt1
- 25.3.2 released

* Thu Jul 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.6.1-alt1
- 24.6.1 released

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.3.0-alt1
- 24.3.0 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.0.0-alt1
- 23.0.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.0.1-alt1
- 21.0.1 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.1.0-alt1
- 18.1.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0.5-alt1
- 16.0.5 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.1.3-alt1
- 15.1.3 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.7.4-alt1
- 13.7.4 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.2-alt1
- 13.0.2 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.4.2-alt1
- 11.4.2 released
