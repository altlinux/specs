%define _unpackaged_files_terminate_build 1

Name: udev-rules-nvidia-sleep
Version: 1.1.0
Release: alt1

Summary: udev rules to fix sleep mode with nvidia gpus
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildArch: noarch

Source: 90-nvidia-sleep.rules

%description
Collection of quirks, that fix sleep mode with nvidia gpus.

%install
install -D -m 0644 %SOURCE0 %buildroot%_udevrulesdir/90-nvidia-sleep.rules

%files
%_udevrulesdir/90-nvidia-sleep.rules

%changelog
* Tue Jul 21 2026 Pavel Petrykin <silverducks@altlinux.org> 1.1.0-alt1
- Add quirk for nvidia 5080.

* Wed Jul 01 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.0-alt1
- Initial build for Alt Linux.
