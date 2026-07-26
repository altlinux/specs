%define _unpackaged_files_terminate_build 1

Name: miunlock
Version: 1.7.3
Release: alt1

Summary: Retrieve Xiaomi encryptData(token) to unlock bootloader
License: Apache-2.0
Group: System/Configuration/Other

URL: https://github.com/offici5l/MiUnlockTool
VCS: https://github.com/offici5l/MiUnlockTool
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: %python3_setup_buildrequires

Requires: android-tools

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
cd MiUnlockTool
%pyproject_build

%install
cd MiUnlockTool
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-%version.dist-info
%doc README.md

%changelog
* Fri Jul 10 2026 David Sultaniiazov <x1z53@altlinux.org> 1.7.3-alt1
- Initial build.
