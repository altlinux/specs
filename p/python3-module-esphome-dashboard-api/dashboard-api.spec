Name: python3-module-esphome-dashboard-api
Version: 1.2.3
Release: alt1

Summary: Python package to interact with the ESPHome dashboard
License: MIT
Group: Development/Python
Url: https://pypi.org/project/esphome-dashboard-api/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/esphome_dashboard_api
%python3_sitelibdir/esphome_dashboard_api-%version.dist-info

%changelog
* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- initial

