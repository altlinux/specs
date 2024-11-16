%define confname ignore-systemd.conf

Name: apt-conf-ignore-systemd
Version: 0.1
Release: alt3

Summary: apt configuration file for systems on sysvinit
License: GPL
Group: System/Configuration/Packaging

Url: http://altlinux.org/sysvinit
Source: %confname

BuildArch: noarch

Requires: sysvinit
Conflicts: systemd systemd-services systemd-sysvinit

%description
This is the apt configuration file for hosts sticking
to sysvinit to avoid installation of systemd packages;
see http://apt-rpm.org/tricks.shtml for details.

%install
install -pDm644 %SOURCE0 %buildroot%_sysconfdir/apt/apt.conf.d/%confname

%files
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%confname

%changelog
* Sat Nov 16 2024 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- back to sisyphus
- minor spec cleanup

* Wed Nov 06 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt2.1
- fix typo in changelog (Closes: 37404)

* Wed Sep 12 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- Added conflicts with ignored packages and requires on sysvinit

* Sat Sep 08 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT (Thanks Speccyfighter)
