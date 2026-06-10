%define rname knights

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Boards
Summary: Chess board
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: gnuchess
Provides:  kde5-knights = %EVR
Obsoletes: kde5-knights < %EVR
Provides:  kde5-knights-common = %EVR
Obsoletes: kde5-knights-common < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-speech-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-ksvg-devel
BuildRequires: kf6-kio-devel kf6-kpackage-devel kf6-kplotting-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwallet-devel kf6-kiconthemes-devel
BuildRequires: plasma6-lib-devel
BuildRequires: kde6-libkdegames-devel

%description
Knights supports local and Internet play against a human being or a computer engine.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSE*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/knights
%_datadir/knights/
%_K6icon/hicolor/*/apps/knights.*
%_K6cfg/knights.kcfg
%_K6xdgapp/*knights*.desktop
%_K6data/knsrcfiles/*knights*.knsrc
%_datadir/metainfo/*knights*.xml


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

