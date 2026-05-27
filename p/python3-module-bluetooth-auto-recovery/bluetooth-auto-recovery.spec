Name: python3-module-bluetooth-auto-recovery
Version: 1.6.4
Release: alt1

Summary: Recover bluetooth adapters that are in an stuck state
License: MIT
Group: Development/Python
URL: https://pypi.org/project/bluetooth-auto-recovery
VCS: https://github.com/bluetooth-devices/bluetooth-auto-recovery

Source0: %name-%version.tar
Source1: pyproject_deps.json

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

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
%python3_sitelibdir/bluetooth_auto_recovery
%python3_sitelibdir/bluetooth_auto_recovery-%version.dist-info

%changelog
* Wed May 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.4-alt1
- 1.6.4 released

* Fri Oct 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.3-alt1
- 1.5.3 released

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.4.2 -> 1.5.2.

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- fixed ftbfs

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- 1.1.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.6-alt1
- 0.3.6 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released
