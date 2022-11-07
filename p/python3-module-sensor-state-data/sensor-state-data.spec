Name: python3-module-sensor-state-data
Version: 2.11.0
Release: alt1

Summary: Models for storing and converting Sensor Data state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sensor-state-data

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
%python3_sitelibdir/sensor_state_data
%python3_sitelibdir/sensor_state_data-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11.0-alt1
- 2.11.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released
