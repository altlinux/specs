Name: python3-module-sensor-state-data
Version: 2.19.0
Release: alt1

Summary: Models for storing and converting Sensor Data state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sensor-state-data
VCS: https://github.com/bluetooth-devices/sensor-state-data

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
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
%python3_sitelibdir/sensor_state_data
%python3_sitelibdir/sensor_state_data-%version.dist-info

%changelog
* Wed Oct 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.19.0-alt1
- 2.19.0 reeased

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.18.1-alt1
- 2.18.1 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.18.0-alt1
- 2.18.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.17.1-alt1
- 2.17.1 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.16.1-alt1
- 2.16.1 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14.0-alt1
- 2.14.0 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11.0-alt1
- 2.11.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released
