%define confname ignore-pulseaudio.conf

Name: apt-conf-ignore-pulseaudio
Version: 0.1
Release: alt1

Summary: apt configuration file for systems on sysvinit
License: GPL
Group: System/Configuration/Packaging

Url: http://git.altlinux.org/people/mike/packages/apt-conf-ignore-pulseaudio.git
Source: %confname
Conflicts: pulseaudio-daemon

BuildArch: noarch
Requires: sysvinit

%description
This is the apt configuration file for systems with pure ALSA
to ignore the installation of pulseaudio server packages;
see http://apt-rpm.org/tricks.shtml for details.

%install
install -pDm644 %SOURCE0 %buildroot%_sysconfdir/apt/apt.conf.d/%confname

%files
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%confname

%changelog
* Thu Apr 15 2021 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on apt-conf-ignore-systemd)
  + thx Speccyfighter and antohami@
