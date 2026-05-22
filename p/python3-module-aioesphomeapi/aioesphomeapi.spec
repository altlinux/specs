Name: python3-module-aioesphomeapi
Version: 45.0.4
Release: alt1

Summary: Python API to ESPHome devices
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aioesphomeapi
VCS: https://github.com/esphome/aioesphomeapi

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
%pyproject_deps_resync_check_pipreqfile requirements/test.txt

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
* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 45.0.4-alt1
- 45.0.4 released

* Tue May 05 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 44.23.0-alt1
- 44.23.0 released

* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 44.16.0-alt1
- 44.16.0 released

* Mon Apr 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 44.15.0-alt1
- 44.15.0 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 44.6.2-alt1
- 44.6.2 released

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
