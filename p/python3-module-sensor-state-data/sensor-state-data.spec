Name: python3-module-sensor-state-data
Version: 2.17.1
Release: alt1

Summary: Models for storing and converting Sensor Data state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sensor-state-data

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/sensor_state_data
%python3_sitelibdir/sensor_state_data-%version.dist-info

%changelog
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
