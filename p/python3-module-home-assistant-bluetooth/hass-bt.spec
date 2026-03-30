Name: python3-module-home-assistant-bluetooth
Version: 2.0.0
Release: alt2

Summary: Home Assistant Bluetooth Models and Helpers
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/home-assistant-bluetooth
VCS: https://github.com/home-assistant-libs/home-assistant-bluetooth

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter pytest-recording
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
%python3_sitelibdir/home_assistant_bluetooth
%python3_sitelibdir/home_assistant_bluetooth-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt2
- revert unsolicited packaging changes

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
