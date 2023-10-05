
Name: webterminal-session
Version: 0.3.0
Release: alt1
%K5init no_altplace

Group: Graphical desktop/Other
Summary: Start WEB-Terminal application
License: GPL-2.0-only
URL: http://git.altlinux.org/gears/w/webterminal-session.git

BuildArch: noarch

Requires: kde5-runtime plasma5-kwin

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5

%description
Start WEB-Terminal application for kiosk mode.

%prep
%setup

#build

%install
mkdir -p %buildroot/%_bindir/
ln -srf %buildroot/%_sysconfdir/webterminal-session/start-webterminal %buildroot/%_bindir/
mkdir -p %buildroot/%_sysconfdir/webterminal-session/
install -m 0755 start-webterminal %buildroot/%_sysconfdir/webterminal-session/
mkdir -p %buildroot/%_datadir/xsessions/
install -m 0755 webterminal.desktop %buildroot/%_datadir/xsessions/
mkdir -p %buildroot/%_x11sysconfdir/wmsession.d/
install -m 0644 99WEBTERMINAL %buildroot/%_x11sysconfdir/wmsession.d/


%files
%dir %_sysconfdir/webterminal-session/
%config(noreplace) %_sysconfdir/webterminal-session/start-webterminal
%_bindir/start-webterminal
%_x11sysconfdir/wmsession.d/*WEBTERMINAL*
%_datadir/xsessions/webterminal.desktop

%changelog
* Thu Oct 05 2023 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- add support for yandex-browser

* Thu Aug 25 2022 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- fix to start

* Thu Aug 25 2022 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- move application command to variable to simplify setup

* Tue Aug 23 2022 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
