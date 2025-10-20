Name: python3-module-bluetooth-sensor-state-data
Version: 1.9.0
Release: alt1

Summary: Models for storing and converting Bluetooth Sensor State Data
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bluetooth-sensor-state-data
VCS: https://github.com/Bluetooth-Devices/bluetooth-sensor-state-data

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
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/bluetooth_sensor_state_data
%python3_sitelibdir/bluetooth_sensor_state_data-%version.dist-info

%changelog
* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.0-alt1
- 1.9.0 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released
