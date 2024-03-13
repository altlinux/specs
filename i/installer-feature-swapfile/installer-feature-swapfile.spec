Name: installer-feature-swapfile
Version: 0.1
Release: alt2

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
* Wed Mar 13 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt2
- fix package description (closes: 49675)

* Tue Mar 12 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
