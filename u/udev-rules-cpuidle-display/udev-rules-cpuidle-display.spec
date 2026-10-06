%define _unpackaged_files_terminate_build 1

Name: udev-rules-cpuidle-display
Version: 1.0.0
Release: alt1

Summary: udev rules to fix display FIFO underruns caused by deep CPU idle states
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildArch: noarch

Source: 90-cpuidle-display.rules

%description
Collection of quirks for machines whose display controller cannot tolerate the
deep CPU idle states the platform advertises. On those machines the display
pipe FIFO runs dry while the CPU is in a deep idle state, which the kernel
reports as "CPU pipe <X> FIFO underrun" and the user sees as a black screen on
the internal panel and on external outputs.

Each quirk caps power/pm_qos_resume_latency_us for every CPU of the affected
machine, so cpuidle stops selecting states the display engine cannot tolerate.
The cap is applied whenever the machine matches, including in configurations
that would not have failed.

%install
install -D -m 0644 %SOURCE0 %buildroot%_udevrulesdir/90-cpuidle-display.rules

%post
# The rules trigger on CPU device events, which do not occur on package install.
udevadm trigger --subsystem-match=cpu --action=add >/dev/null 2>&1 ||:

%files
%_udevrulesdir/90-cpuidle-display.rules

%changelog
* Tue Oct 06 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.0-alt1
- Add quirk for Graviton N15i-K2 (Closes: 45236).
