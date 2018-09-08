%define confname ignore-systemd.conf

Name: apt-conf-ignore-systemd
Version: 0.1
Release: alt1

BuildArch: noarch

Summary: apt configuration file for systems on sysvinit

License: GPL
Group: System/Configuration/Packaging
Url: http://git.altlinux.org/people/antohami/packages/apt-conf-ignore-systemd.git

Source0: %confname

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
* Sat Sep 08 2018 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT (Thanks Speccyfighter)
