Name: python3-module-uart-devices
Version: 0.1.1
Release: alt1

Summary: UART Devices for Linux
License: MIT
Group: Development/Python
Url: https://pypi.org/project/uart-devices
VCS: https://github.com/bluetooth-devices/uart-devices

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
%python3_sitelibdir/uart_devices
%python3_sitelibdir/uart_devices-%version.dist-info

%changelog
* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.1-alt1
- 0.1.1 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.0-alt1
- 0.1.0 released
