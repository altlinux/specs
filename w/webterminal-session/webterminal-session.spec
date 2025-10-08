
Name: webterminal-session
Version: 0.6.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/Other
Summary: Apply WEB-Terminal application
License: GPL-2.0-only
URL: http://git.altlinux.org/gears/w/webterminal-session.git

BuildArch: noarch

Requires: kde6-runtime kwin
Provides: installer-feature-webterminal-setup = 0.5
Obsoletes: installer-feature-webterminal-setup < 0.5

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

%description
Apply WEB-Terminal application for kiosk mode.

%prep
%setup

%install
mkdir -p %buildroot/%_bindir/
ln -srf %buildroot/%_sysconfdir/webterminal-session/start-webterminal %buildroot/%_bindir/
mkdir -p %buildroot/%_sysconfdir/webterminal-session/
install -m 0755 start-webterminal %buildroot/%_sysconfdir/webterminal-session/
mkdir -p %buildroot/%_datadir/xsessions/
install -m 0755 webterminal.desktop %buildroot/%_datadir/xsessions/
mkdir -p %buildroot/%_x11sysconfdir/wmsession.d/
install -m 0644 99WEBTERMINAL %buildroot/%_x11sysconfdir/wmsession.d/
mkdir -p %buildroot/%_sysconfdir/alterator/kiosk/profiles/
install -m 0644 kiosk-webterminal-addon %buildroot/%_sysconfdir/alterator/kiosk/profiles/webterminal-addon
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -m 0755 firsttime-setup.sh %buildroot/%_sysconfdir/firsttime.d/webterminal-setup.sh

%files
%dir %_sysconfdir/webterminal-session/
%config(noreplace) %_sysconfdir/webterminal-session/start-webterminal
%config(noreplace) %_sysconfdir/alterator/kiosk/profiles/webterminal-addon
%_sysconfdir/firsttime.d/*.sh
%_bindir/start-webterminal
%_x11sysconfdir/wmsession.d/*WEBTERMINAL*
%_datadir/xsessions/webterminal.desktop

%changelog
* Wed Oct 08 2025 Sergey V Turchin <zerg at altlinux dot org> 0.6.0-alt1
- setup kiosk on first start

* Fri Sep 12 2025 Sergey V Turchin <zerg at altlinux dot org> 0.5.0-alt1
- start maliit-keyboard if present

* Tue May 27 2025 Sergey V Turchin <zerg at altlinux dot org> 0.4.3-alt2
- update requires

* Wed Apr 16 2025 Sergey V Turchin <zerg at altlinux dot org> 0.4.3-alt1
- add chromium

* Fri Mar 21 2025 Sergey V Turchin <zerg at altlinux dot org> 0.4.2-alt1
- add --no-first-run startup option

* Thu Mar 13 2025 Sergey V Turchin <zerg at altlinux dot org> 0.4.1-alt1
- don't source /usr/bin/kde5

* Tue Dec 03 2024 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt1
- update requires

* Tue Jan 16 2024 Sergey V Turchin <zerg at altlinux dot org> 0.3.1-alt1
- update startup options

* Thu Oct 05 2023 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- add support for yandex-browser

* Thu Aug 25 2022 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- fix to start

* Thu Aug 25 2022 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- move application command to variable to simplify setup

* Tue Aug 23 2022 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
