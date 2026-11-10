Name: python3-module-tuya-sharing
Version: 0.2.15
Release: alt1

Summary: Tuya Device Sharing SDK
License: MIT
Group: Development/Python
URL: https://pypi.org/project/tuya-device-sharing-sdk
VCS: https://github.com/tuya/tuya-device-sharing-sdk

Provides: python3-module-tuya-device-sharing-sdk = %EVR

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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
%python3_sitelibdir/tuya_sharing
%python3_sitelibdir/tuya_device_sharing_sdk-%version.dist-info

%changelog
* Tue Nov 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.15-alt1
- 0.2.15 released

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1.1
- Demodernized packaging.

* Fri Feb 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.9-alt1
- 0.2.9 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released
