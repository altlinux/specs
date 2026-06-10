%define rname lskat

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Cards
Summary: Lieutnant skat
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: kde-carddecks
Provides:  kde5-lskat = %EVR
Obsoletes: kde5-lskat < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: qt6-phonon-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel

%description
Lieutnant Skat (from German "Offiziersskat") is a fun and engaging card game for two players,
where the second player is either live opponent, or built in artificial intelligence.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data lskat
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/lskat
%_K6xdgapp/org.kde.lskat.desktop
%_K6icon/*/*/apps/lskat.*
%_K6data/lskat/
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

