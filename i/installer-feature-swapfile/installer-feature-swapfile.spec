Name: installer-feature-swapfile
Version: 0.1
Release: alt1

Summary: Clear xprofile
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Clear /etc/skel/.xprofile for new users.

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
* Tue Mar 12 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
