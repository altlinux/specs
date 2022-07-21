Name: installer-feature-systemd-oomd
Version: 0.2
Release: alt1

Summary: Turn on PSI for systemd-oomd
License: GPL-3.0-only
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
Turn on kernel Pressure Stall Information for systemd-oomd.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot/%hookdir
install -pm755 *.sh %buildroot/%hookdir/

%files
%hookdir/*

%changelog
* Thu Jul 21 2022 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix usage of update-grub

* Wed Jul 20 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
