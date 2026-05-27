Name: python3-module-bluetooth-data-tools
Version: 1.29.18
Release: alt1

Summary: Tools for converting bluetooth data and packets
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/bluetooth-data-tools
VCS: https://github.com/bluetooth-devices/bluetooth-data-tools

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
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
%pyproject_run_pytest tests

%files
%python3_sitelibdir/bluetooth_data_tools
%python3_sitelibdir/bluetooth_data_tools-%version.dist-info

%changelog
* Wed May 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.18-alt1
- 1.29.18 released

* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.17-alt1
- 1.29.17 released

* Thu May 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.15-alt1
- 1.29.15 released

* Wed May 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.11-alt1
- 1.29.11 released

* Tue May 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.8-alt1
- 1.29.8 released

* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.7-alt1
- 1.29.7 released

* Fri May 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.29.1-alt1
- 1.29.1 released

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.28.4-alt1
- 1.28.4 released

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 1.28.2-alt1
- 1.20.0 -> 1.28.2.

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.20.0-alt1
- 1.20.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.19.3-alt1
- 1.19.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19.0-alt1
- 1.19.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13.0-alt1
- 1.13.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11.0-alt1
- 1.11.0 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

