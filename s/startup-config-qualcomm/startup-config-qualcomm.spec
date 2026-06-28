%define _unpackaged_files_terminate_build 1

Name: startup-config-qualcomm
Version: 2
Release: alt1
Summary: Startup script for qualcomm
License: MIT
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd

%description
This package provides a standart way to make device-specific config changes on
qualcomm devices. It can set voice routing setup for q6voiced.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_unitdir
install -m 0755 configure-firmware-path.sh %buildroot%_sbindir/configure-firmware-path
install -m 0755 configure-q6voiced.sh %buildroot%_sbindir/configure-q6voiced
install -m 0644 configure-firmware-path.service %buildroot%_unitdir
install -m 0644 configure-q6voiced.service %buildroot%_unitdir

%files
%_sbindir/configure-firmware-path
%_sbindir/configure-q6voiced
%_unitdir/configure-firmware-path.service
%_unitdir/configure-q6voiced.service

%changelog
* Sun Jun 28 2026 Vasiliy Doylov <neko@altlinux.org> 2-alt1
- Split q6voice and firmware configuration.

* Sun May 10 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT.
