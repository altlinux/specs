Name: installer-feature-lightdm-kde
Version: 0.1
Release: alt1

Summary: Setup LightDM after install
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Setup LightDM after system installation.

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
* Tue May 30 2023 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
