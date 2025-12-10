Name: python3-module-esphome-dashboard-api
Version: 1.3.0
Release: alt1

Summary: Python package to interact with the ESPHome dashboard
License: MIT
Group: Development/Python
Url: https://pypi.org/project/esphome-dashboard-api
VCS: https://github.com/esphome/dashboard-api

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

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/esphome_dashboard_api
%python3_sitelibdir/esphome_dashboard_api-%version.dist-info

%changelog
* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- initial
