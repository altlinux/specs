Name: firsttime-lightdm-kde
Version: 0.3.2
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
* Wed Apr 15 2026 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- don't setup lightdm for old NVIDIA (kwin fixed to fail)

* Tue Mar 03 2026 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- fix editing kde-greeter-fallback.conf

* Fri Feb 27 2026 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- setup greeter-session and greeter-session-fallback for old NVIDIA

* Mon Jun 02 2025 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- set default x11 session for old nvidia cards

* Tue Jul 23 2024 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- fix actions

* Mon Jul 22 2024 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix state file permissions

* Tue Jul 09 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
