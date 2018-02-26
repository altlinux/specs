Name: cpufreq-simple
Version: 0.1.4
Release: alt1

Summary: Simple scripts for managing CPUfreq settings
License: %gpl2plus
Group: System/Base

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: cpufrequtils libshell

%description
Install this package if you would like it to attempt
cpufreq autoconfiguration in order to save power
as well as reduce heat and noise.

%prep
%setup

%install
install -pDm755 %name %buildroot%_bindir/cpufreq-simple
install -pDm755 detect-cpufreq-module %buildroot%_bindir/detect-cpufreq-module
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.udev-rules %buildroot%_sysconfdir/udev/rules.d/96-%name.rules
install -pDm644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pDm755 %name.pm-utils %buildroot%_sysconfdir/pm/sleep.d/90%name

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_bindir/*
%_initdir/%name
%_sysconfdir/udev/rules.d/*.rules
%_sysconfdir/pm/sleep.d/*

%changelog
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

