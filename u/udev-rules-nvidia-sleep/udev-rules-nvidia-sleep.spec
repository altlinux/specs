%define _unpackaged_files_terminate_build 1

Name: udev-rules-nvidia-sleep
Version: 1.0.0
Release: alt1

Summary: udev rule for 4060 Ti
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildArch: noarch

Source: 90-nvidia-sleep-4060-ti.rules

%description
Quirk for 4060 Ti nvidia gpu to fix graphical issues during wake from S3 sleep.

%install
install -D -m 0644 %SOURCE0 %buildroot%_udevrulesdir/90-nvidia-sleep-4060-ti.rules

%files
%_udevrulesdir/90-nvidia-sleep-4060-ti.rules

%changelog
* Wed Jul 01 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.0-alt1
- Initial build for Alt Linux.
