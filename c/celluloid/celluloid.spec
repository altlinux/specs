%define xdg_name io.github.celluloid_player.Celluloid

Name: celluloid
Version: 0.27
Release: alt2

Summary: Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv.
License: GPLv3
Group: Video

Url: https://github.com/celluloid-player/celluloid
Source: %name-%version.tar
Packager: Vladimir Didenko <cow@altlinux.org>

Provides: gnome-mpv = %version-%release
Obsoletes: gnome-mpv <= 0.16

BuildRequires: libappstream-glib-devel
BuildRequires: meson
BuildRequires: python3-dev
BuildRequires: glib2-devel
BuildRequires: libgtk4-devel
BuildRequires: libmpv-devel
BuildRequires: libepoxy-devel
BuildRequires: libadwaita-devel

Requires: yt-dlp

%description
Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv. Celluloid
interacts with mpv via the client API exported by libmpv, allowing access
to mpv's powerful playback capabilities.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_datadir/metainfo/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/dbus-1/services/%xdg_name.service
%_man1dir/*.1.*

%changelog
* Wed Jul 31 2024 Vladimir Didenko <cow@altlinux.org> 0.27-alt2
- add yt-dlp to requires for online video downloading (closes: #51012)

* Thu Jun 27 2024 Vladimir Didenko <cow@altlinux.org> 0.27-alt1
- new version

* Thu Sep 21 2023 Vladimir Didenko <cow@altlinux.org> 0.26-alt1
- new version

* Thu Apr 6 2023 Vladimir Didenko <cow@altlinux.org> 0.25-alt1
- new version

* Mon Aug 22 2022 Vladimir Didenko <cow@altlinux.org> 0.24-alt1
- new version

* Wed Mar 9 2022 Vladimir Didenko <cow@altlinux.org> 0.23-alt1
- new version

* Tue Nov 9 2021 Vladimir Didenko <cow@altlinux.org> 0.22-alt1
- new version

* Wed Mar 24 2021 Vladimir Didenko <cow@altlinux.org> 0.21-alt1
- new version

* Wed Nov 25 2020 Vladimir Didenko <cow@altlinux.org> 0.20-alt1
- new version

* Tue Apr 14 2020 Vladimir Didenko <cow@altlinux.org> 0.19-alt1
- new version

* Mon Nov 11 2019 Vladimir Didenko <cow@altlinux.org> 0.18-alt1
- new version

* Thu Oct 3 2019 Vladimir Didenko <cow@altlinux.org> 0.17-alt1
- new version
- package is renamed following upstream

* Mon Jan 28 2019 Vladimir Didenko <cow@altlinux.org> 0.16-alt1
- new version

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.qa1
- NMU: applied repocop patch

* Wed Sep 19 2018 Vladimir Didenko <cow@altlinux.org> 0.15-alt1
- new version

* Thu Mar 15 2018 Vladimir Didenko <cow@altlinux.org> 0.14-alt1
- new version

* Fri Dec 1 2017 Vladimir Didenko <cow@altlinux.org> 0.13-alt1
- new version

* Fri Jul 28 2017 Vladimir Didenko <cow@altlinux.org> 0.12-alt1
- new version
- switch to meson build

* Fri Mar 11 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7-alt2
- initial build for ALT Linux Sisyphus
