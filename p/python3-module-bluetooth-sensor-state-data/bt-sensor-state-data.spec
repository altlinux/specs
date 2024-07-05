Name: python3-module-bluetooth-sensor-state-data
Version: 1.7.1
Release: alt1

Summary: Models for storing and converting Bluetooth Sensor State Data
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bluetooth-sensor-state-data

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/bluetooth_sensor_state_data
%python3_sitelibdir/bluetooth_sensor_state_data-%version.dist-info

%changelog
* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released
