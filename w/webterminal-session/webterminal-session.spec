
Name: webterminal-session
Version: 0.7.2
Release: alt1
%K6init no_altplace

Group: Graphical desktop/Other
Summary: WEB-Terminal session
License: GPL-2.0-only
URL: http://git.altlinux.org/gears/w/webterminal-session.git

BuildArch: noarch

Requires: webterminal-application > 0
Requires: kde6-runtime kwin plasma6-layer-shell-qt
#Requires: plasma-keyboard
Provides: installer-feature-webterminal-setup = 0.5
Obsoletes: installer-feature-webterminal-setup < 0.5

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

%description
Apply WEB-Terminal application for kiosk mode session.

%package -n webterminal-application
Group: Graphical desktop/Other
Summary: Application for WEB-Terminal session
%description -n webterminal-application
Application for WEB-Terminal session.

%prep
%setup

%install
mkdir -p %buildroot/%_bindir/
install -m 0755 start-webterminal %buildroot/%_bindir/
install -m 0755 webterminal-application %buildroot/%_bindir/
mkdir -p %buildroot/%_sysconfdir/sysconfig/
install -m 0644 webterminal-app %buildroot/%_sysconfdir/sysconfig/
mkdir -p %buildroot/%_datadir/wayland-sessions/
install -m 0644 webterminal.desktop %buildroot/%_datadir/wayland-sessions/
mkdir -p %buildroot/%_sysconfdir/alterator/kiosk/profiles/
install -m 0644 kiosk-webterminal-addon %buildroot/%_sysconfdir/alterator/kiosk/profiles/webterminal-addon
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -m 0755 firsttime-setup.sh %buildroot/%_sysconfdir/firsttime.d/webterminal-setup.sh
mkdir -p %buildroot/%_userunitdir/{webterminal-session.target.d,webterminal-session.target.wants}
install -m 0644 webterminal-session.target %buildroot/%_userunitdir
install -m 0644 webterminal-gui.service %buildroot/%_userunitdir

%files
#%config(noreplace) %_sysconfdir/sysconfig/webterminal
%config(noreplace) %_sysconfdir/alterator/kiosk/profiles/webterminal-addon
%_sysconfdir/firsttime.d/*.sh
%_bindir/start-webterminal
%_datadir/wayland-sessions/webterminal.desktop
%dir %_userunitdir/webterminal-session.target.d/
%dir %_userunitdir/webterminal-session.target.wants/
%_userunitdir/webterminal-session.target
%_userunitdir/webterminal-gui.service

%files -n webterminal-application
%config(noreplace) %_sysconfdir/sysconfig/webterminal-app
%_bindir/webterminal-application

%changelog
* Tue Jun 02 2026 Sergey V Turchin <zerg at altlinux dot org> 0.7.2-alt1
- using basic password store

* Mon May 04 2026 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt1
- separate webterminal-application

* Wed Apr 29 2026 Sergey V Turchin <zerg at altlinux dot org> 0.7.0-alt1
- switch to wayland
- switch to systemd user session
- setup sound

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
