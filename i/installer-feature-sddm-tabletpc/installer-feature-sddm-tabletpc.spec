Name: installer-feature-sddm-tabletpc
Version: 0.2
Release: alt1

Summary: Setup default session for SDDM and TabletPC
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Setup default session for SDDM and TabletPC.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Dec 24 2021 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix setup session

* Fri Dec 24 2021 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
