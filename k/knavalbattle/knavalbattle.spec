%define rname knavalbattle

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Strategy
Summary: Battleship game with built-in game server
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-knavalbattle = %EVR
Obsoletes: kde5-knavalbattle < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdnssd-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-sonnet-devel kf6-kcrash-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data knavalbattle kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/knavalbattle
%_K6data/knavalbattle/
%_K6icon/*/*/apps/knavalbattle.*
%_K6xdgapp/org.kde.knavalbattle.desktop
%_datadir/metainfo/*.xml


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Thu Oct 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri May 30 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Feb 25 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

