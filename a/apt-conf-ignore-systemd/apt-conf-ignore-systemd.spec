%define confname ignore-systemd.conf

Name: apt-conf-ignore-systemd
Version: 0.1
Release: alt2.1

BuildArch: noarch

Summary: apt configuration file for systems on sysvinit

License: GPL
Group: System/Configuration/Packaging
Url: http://git.altlinux.org/people/antohami/packages/apt-conf-ignore-systemd.git

Source0: %confname
Conflicts: systemd systemd-services systemd-sysvinit
Requires: sysvinit

%description
This is the apt configuration file for systems on sysvinit,
to ignore the installation of systemd packages,
see http://apt-rpm.org/tricks.shtml for details.

%install
mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
install -p -m644 %SOURCE0 %buildroot%_sysconfdir/apt/apt.conf.d/%confname

%files
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%confname

%changelog
* Wed Nov 06 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt2.1
- fix typo in changelog (Closes: 37404)

* Wed Sep 12 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- Added conflicts with ignored packages and requires on sysvinit

* Sat Sep 08 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT (Thanks Speccyfighter)
