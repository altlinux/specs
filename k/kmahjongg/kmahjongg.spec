%define rname kmahjongg

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Boards
Summary: A tile laying patience
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmahjongg = %EVR
Obsoletes: kde5-kmahjongg < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kcompletion-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel  kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-knewstuff-devel kf6-kpackage-devel kf6-kservice-devel kf6-kxmlgui-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel kde6-libkmahjongg-devel

%description
KMahjongg is a fun board game created after the famous oriental game of Mahjong.
Unlike the original however, KMahjongg is a tile matching game for one player,
a variation usually known as Mahjong Solitaire.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kmahjongg
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kmahjongg
%_K6data/kmahjongg/
%_K6xdgapp/*kmahjongg*.desktop
%_K6cfg/*kmahjongg*
%_K6icon/*/*/apps/*kmahjongg*
%_datadir/qlogging-categories6/*.*categories
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

