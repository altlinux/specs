Name: python3-module-usb-devices
Version: 0.5.0
Release: alt1

Summary: Bluetooth USB adapters
License: MIT
Group: Development/Python
URL: https://pypi.org/project/usb-devices
VCS: https://github.com/bluetooth-devices/usb-devices

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
%python3_sitelibdir/usb_devices
%python3_sitelibdir/usb_devices-%version.dist-info

%changelog
* Wed May 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt1
- 0.4.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
