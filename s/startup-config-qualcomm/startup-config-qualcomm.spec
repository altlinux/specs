%define _unpackaged_files_terminate_build 1

Name: startup-config-qualcomm
Version: 1
Release: alt1
Summary: Startup script for qualcomm
License: MIT
Group: System/Kernel and hardware

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd

%description
This package provides a standart way to make device-specific config changes on
qualcomm devices.
It can set voice routing setup for q6voiced and override firmware search path.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_unitdir
install -m 0755 startup_config_qualcomm.sh %buildroot%_sbindir/startup_config_qualcomm
install -m 0644 startup-config-qualcomm.service %buildroot%_unitdir

%files
%_sbindir/startup_config_qualcomm
%_unitdir/startup-config-qualcomm.service

%changelog
* Sun May 10 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT
