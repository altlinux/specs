Name: python3-module-bleak-esphome
Version: 3.7.6
Release: alt1

Summary: Bleak backend of ESPHome
License: MIT
Group: Development/Python
URL: https://pypi.org/project/bleak-esphome
VCS: https://github.com/bluetooth-devices/bleak-esphome

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
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/bleak_esphome
%python3_sitelibdir/bleak_esphome-%version.dist-info

%changelog
* Fri May 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.6-alt1
- 3.7.6 released

* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.5-alt1
- 3.7.5 released

* Fri May 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.4-alt1
- 3.7.4 released

* Wed Apr 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.3-alt1
- 3.7.3 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.1-alt1
- 3.7.1 released

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.0-alt1
- 3.6.0 released

* Mon Dec 08 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.0-alt1
- 3.4.0 released

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.0 -> 3.3.0.

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 2.0.0 -> 3.2.0.

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
