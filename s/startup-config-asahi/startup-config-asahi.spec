%define _unpackaged_files_terminate_build 1

Name: startup-config-asahi
Version: 1
Release: alt1
Summary: Startup script for asahi
License: MIT
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd

%description
This package provides a standart way to make device-specific config changes on
apple silicon devices.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_unitdir
install -m 0755 asahi-install-firmware.sh %buildroot%_sbindir/asahi-install-firmware
install -m 0644 asahi-install-firmware.service %buildroot%_unitdir

%files
%_sbindir/asahi-install-firmware
%_unitdir/asahi-install-firmware.service

%changelog
* Fri Aug 28 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT.
