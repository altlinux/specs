Name: pa-conf-switch-on-connect
Version: 0.1
Release: alt1
Summary: Additional PulseAudio configuration snippet
License: LGPLv2.1+
Group: System/Configuration/Hardware
Source0: switch-on-connect.pa
BuildArch: noarch

Requires: pulseaudio-daemon >= 14.2-alt6

%description
This package contains the PulseAudio configuratin file to load
module-switch-on-connect which allow to use hot-plugged devices, like Bluetooth
or USB, automatically.

%install
install -Dm0644 %SOURCE0 %buildroot/%_sysconfdir/pulse/default.pa.d/50-switch-on-connect.pa

%files
%config(noreplace) %_sysconfdir/pulse/default.pa.d/

%changelog
* Wed Mar 30 2022 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.
