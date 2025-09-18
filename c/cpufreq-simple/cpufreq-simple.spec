Name: cpufreq-simple
Version: 1.1.0
Release: alt1

Summary: Simple scripts for managing CPUfreq settings
License: GPL-2.0-or-later
Group: System/Base

Source: %name-%version.tar
BuildArch: noarch

Requires: cpupower libshell
# For on_ac_power
Requires: powermgmt-base >= 1.38-alt1

%description
Install this package if you would like it to attempt
cpufreq autoconfiguration in order to save power
as well as reduce heat and noise.

%prep
%setup

%install
install -pDm755 %name %buildroot%_sbindir/cpufreq-simple
install -pDm755 detect-cpufreq-module %buildroot%_bindir/detect-cpufreq-module
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.udev-rules %buildroot%_udevrulesdir/96-%name.rules
install -pDm644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pDm755 %name.pm-utils %buildroot%_libexecdir/pm-utils/sleep.d/90%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service
install -pDm644 %name-wake.service %buildroot%_unitdir/%name-wake.service

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_bindir/*
%_sbindir/*
%_initdir/%name
%_unitdir/*.service
%_udevrulesdir/*.rules
%_libexecdir/pm-utils/sleep.d/*

%changelog
* Thu Sep 18 2025 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- cpufreq-simple: Show available and current EPP.
- cpufreq-simple: Show available governors.
- cpufreq-simple: Add energy performance policy support.
- cpufreq-simple: Refactor setting governor code.

* Mon Sep 15 2025 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- cpufreq-simple: Don't report an error if driver not detected.
- Don't use rpm-build-licenses.
- cpufreq-simple: Drop EXTRA_MODULES variable support.
- cpufreq-simple: Always try to load cpufreq module.
- cpufreq-simple: Add status command.
- cpufreq-simple: Support amd-pstate-epp driver (closes: #54124).
- cpufreq-simple: Use on_ac_power to get power state.

* Thu Nov 06 2014 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- cpufreq-simple.sysconfig: Update comments.
- Set 'powersave' governor as default on AC for intel_pstate.

* Mon Apr 21 2014 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Use cpupower instead of cpufrequtils.

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Move cpufreq-simple from %%_bindir to %%_sbindir.
- Ensure that PATH is correct.
- Use proper directories for udev rule and pm-utils script.

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Install cpufreq-simple-wake.service too.
- Use different "default" governors for different drivers.
- Add cpufreq-simple-wake.service.

* Fri Jun 14 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- Drop pm-utils deps again.

* Mon Jun 10 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Don't try to load already loaded module.
- Require pm-utils.

* Mon Mar 11 2013 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Install and package systemd service file.

* Tue Mar 05 2013 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Use cpu/modalias if possible (closes: #28232).
- Added systemd service file.
- Load powernow-k8 for AMD Bulldozer (21) and Llano (18) CPUs.

* Thu Jul 19 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.6-alt1
- Don't treat "live" mode specially.

* Wed Jul 04 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.5-alt1
- Presume AC power harder when it's unknown in various ways.

* Wed Jul 04 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.4-alt1
- Driver autodetection can now get [PASSED] instead of [FAILED].

* Sun Apr 01 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.3-alt1
- Extend the previous tweak by autodetecting livecd mode.

* Sun Apr 01 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.2-alt1
- Tweak the previous complement by making the behaviour configurable.

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.1.4.1-alt1
- Complement the previous fix by not erorring out in case
  no cpufreq module is configured or detected.

* Mon Mar 05 2012 Michael Shigorin <mike@altlinux.org> 0.1.4-alt1
- Avoid configuring any cpufreq module for non-mobile Pentium 4
  due to the lack of SpeedStep support in those (see also #6074)

* Wed Nov 09 2011 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt2
- Package pm-utils script.

* Tue Nov 08 2011 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Setup cpufreq during resume.
- Set AC_OFF state CPU governor to 'ondemand' again.

* Sat Nov 05 2011 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Default AC_OFF state CPU governor changed to 'conservative'.
- Treat unknown AC state as on-line.
- init script: Use is_loaded in start().
- init script: Don't run modprobe if EXTRA_MODULES not setted.

* Fri Nov 04 2011 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- Minor fixups all over the place.
- Enabled the service by default.

* Thu Nov 03 2011 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

