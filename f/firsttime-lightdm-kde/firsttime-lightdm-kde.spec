Name: firsttime-lightdm-kde
Version: 0.2.1
Release: alt1

Group: System/Configuration/Other
Summary: Setup LightDM after install
Url: http://www.altlinux.org/
License: GPL-2.0-or-later

BuildArch: noarch

Source: %name-%version.tar

%description
Setup LightDM after system installation.

%prep
%setup

%build

%install
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -pm755 *.sh %buildroot/%_sysconfdir/firsttime.d/

%files
%_sysconfdir/firsttime.d/*

%changelog
* Tue Jul 23 2024 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- fix actions

* Mon Jul 22 2024 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix state file permissions

* Tue Jul 09 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
