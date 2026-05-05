Name: python3-module-bleak
Version: 3.0.2
Release: alt1

Summary: Bluetooth Low Energy platform Agnostic Klient
License: MIT
Group: Development/Python
URL: https://pypi.org/project/bleak
VCS: https://github.com/hbldh/bleak

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
%add_pyproject_deps_check_filter bumble
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup test
# requires actual bt hardware
rm -fr tests/integration

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/bleak
%python3_sitelibdir/bleak-%version.dist-info

%changelog
* Tue May 05 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.2-alt1
- 3.0.2 released

* Wed Apr 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.1-alt1
- 2.1.1 released

* Fri Dec 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.1.0 -> 1.1.1.

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.22.3 -> 1.1.0.

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.3-alt1
- 0.22.3 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.2-alt1
- 0.22.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.1-alt1
- 0.21.1 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.2-alt1
- 0.20.2 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.5-alt1
- 0.19.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.2-alt1
- 0.19.2 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.1-alt1
- 0.19.1 released

* Fri Sep 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt2
- filtered out rest of android-specific reqs

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt1
- 0.17.0 released
