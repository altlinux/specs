%def_with check

Name: python3-module-home-assistant-bluetooth
Version: 2.0.0
Release: alt1.1

Summary: Home Assistant Bluetooth Models and Helpers
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/home-assistant-bluetooth
VCS: https://github.com/home-assistant-libs/home-assistant-bluetooth

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-bleak
BuildRequires: python3-module-habluetooth
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
%python3_sitelibdir/home_assistant_bluetooth
%python3_sitelibdir/home_assistant_bluetooth-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.1
- Demodernized packaging.

* Wed Oct 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.13.0-alt1
- 1.13.0 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.2-alt1
- 1.12.2 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.0-alt1
- 1.12.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.0-alt1
- 1.10.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.2-alt1
- 1.9.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
