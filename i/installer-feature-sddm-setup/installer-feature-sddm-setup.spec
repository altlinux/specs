Name: installer-feature-sddm-setup
Version: 0.4
Release: alt1

Summary: Setup SDDM after install
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Provides: installer-feature-sddm-tabletpc = %EVR
Obsoletes: installer-feature-sddm-tabletpc < %EVR

Source: %name-%version.tar

%description
Setup SDDM after system installation.

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
* Fri Feb 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- fix get first user name

* Thu Feb 24 2022 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- set default user when empty

* Fri Dec 24 2021 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix setup session

* Fri Dec 24 2021 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
