%define rname libkdegames

%define kdegames_sover 6
%define libkdegames libkdegames6_%kdegames_sover
%define kdegamesprivate_sover 6
%define libkdegamesprivate libkdegames6private%kdegamesprivate_sover


Name: kde6-%rname
Version: 26.04.2
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE games library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: libopenal-devel libsndfile-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel kf6-kdnssd-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
#Provides:  kde5-libkdegames-common = %EVR
#Obsoletes: kde5-libkdegames-common < %EVR
%description common
%name common package

%package -n kde-carddecks
Group: Games/Cards
Summary: Carddecks for KDE cardgames
BuildArch: noarch
Requires: %name-common >= %EVR
Provides:  kde5-carddecks = %EVR
Obsoletes: kde5-carddecks < %EVR
%description -n kde-carddecks
Carddecks for KDE cardgames.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdegames
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdegames
%name library

%package -n %libkdegamesprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkdegamesprivate
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data carddecks kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files -n kde-carddecks
%_K6data/carddecks/

%files devel
%_K6inc/KDEGames?/
%_K6link/lib*.so
%_K6lib/cmake/KDEGames?/

%files -n %libkdegames
%_K6lib/libKDEGames?.so.%kdegames_sover
%_K6lib/libKDEGames?.so.*
%_K6qml/org/kde/games/

%files -n %libkdegamesprivate
%_K6lib/libKDEGames?Private.so.%kdegamesprivate_sover
%_K6lib/libKDEGames?Private.so.*

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

