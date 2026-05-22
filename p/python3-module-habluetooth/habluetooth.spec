Name: python3-module-habluetooth
Version: 6.2.1
Release: alt1

Summary: High availability Bluetooth
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/habluetooth
VCS: https://github.com/bluetooth-devices/habluetooth

Source0: %name-%version.tar
Source1: pyproject_deps.json

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api 3.12

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

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
* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 6.2.1-alt1
- 6.2.1 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 5.11.2-alt1
- 5.11.2 released

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
