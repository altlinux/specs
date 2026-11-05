%define _unpackaged_files_terminate_build 1

Name: nvidia-sleep-quirks
Version: 2.0.0
Release: alt1

Summary: Collection of quirks that fix sleep mode with nvidia gpus
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildArch: noarch

Source: 90-nvidia-sleep.conf
Source1: nvidia-sleep-quirks

Obsoletes: udev-rules-nvidia-sleep < %EVR
Provides: udev-rules-nvidia-sleep = %EVR

%description
Collection of quirks, that fix sleep mode with nvidia gpus.

%install
install -D -m 0644 %SOURCE0 \
  %buildroot%_sysconfdir/modprobe.d/90-nvidia-sleep.conf
install -D -m 0755 %SOURCE1 \
  %buildroot%_prefix/libexec/nvidia-sleep-quirks

%post
# Remove old version's udev-rule-generated file
rm -f /etc/modprobe.d/90-nvidia-pvma-quirk.conf

%files
%_sysconfdir/modprobe.d/90-nvidia-sleep.conf
%_prefix/libexec/nvidia-sleep-quirks

%changelog
* Fri Oct 30 2026 Pavel Petrykin <silverducks@altlinux.org> 2.0.0-alt1
- Switch to a static modprobe config to ensure quirk is loaded on first boot (Closes: 61126).
- Rename package accordingly.
- Add quirk to set UseKernelSuspendNotifiers=1 for open nvidia kernel module v595+ (Closes: 60037).

* Tue Jul 21 2026 Pavel Petrykin <silverducks@altlinux.org> 1.1.0-alt1
- Add quirk for nvidia 5080.

* Wed Jul 01 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.0-alt1
- Initial build for Alt Linux.
