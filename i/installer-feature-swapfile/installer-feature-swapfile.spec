Name: installer-feature-swapfile
Version: 0.2.2
Release: alt1

Summary: Create swap-file
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Create /swap file and add to /etc/fstab.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Sep 24 2024 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- fix detect VM

* Thu Mar 14 2024 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- fix fstab entry

* Wed Mar 13 2024 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- add btrfs support

* Wed Mar 13 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt2
- fix package description (closes: 49675)

* Tue Mar 12 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
