%define rname haruna

%define sover 0
%define libharuna libharuna%sover

Name: kde5-%rname
Version: 0.10.2
Release: alt1
%K5init altplace

Group: Video
Summary: Video Player
Url: https://invent.kde.org/multimedia/haruna
License: GPL-3.0-or-later

Requires: %name-youtube-player

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel qt5-x11extras-devel
BuildRequires: libmpv-devel
BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libavfilter-devel libswscale-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdoctools-devel kf5-kfilemetadata-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kirigami-devel kf5-kxmlgui-devel
BuildRequires: plasma5-breeze-devel

%description
Haruna is an open source video player built with Qt/QML and libmpv.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package -n %name-youtube-player-4-ytdlp
Group: System/Configuration/Other
Summary: %name youtube player
Provides: %name-youtube-player
Provides: %name-youtube-player-ytdlp
Requires: %name-common
Requires: yt-dlp
%description -n %name-youtube-player-4-ytdlp
%name youtube player.

%package -n %name-youtube-player-2-youtubedl
Group: System/Configuration/Other
Summary: %name youtube player
Provides: %name-youtube-player
Provides: %name-youtube-player-youtubedl
Requires: %name-common
Requires: youtube-dl
%description -n %name-youtube-player-2-youtubedl
%name youtube player.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libharuna
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libharuna
KF5 library

%prep
%setup -n %rname-%version

%build
%K5build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name

%files common
%doc LICENSES/*
%files -n %name-youtube-player-4-ytdlp
%files -n %name-youtube-player-2-youtubedl
%files -f %name.lang
%doc README.md
%_K5bin/haruna
%_K5xdgapp/*haruna*.desktop
%_K5icon/hicolor/*/apps/*haruna*.*

#%files -n %libharuna
#%doc LICENSE* README.md
#%_K5lib/libharuna.so.%sover
#%_K5lib/libharuna.so.*

%changelog
* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt1
- new version

* Wed Nov 09 2022 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- new version

* Thu Aug 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Sun Jul 17 2022 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- prefer yt-dlp over youtube-dl

* Thu Apr 21 2022 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Tue Apr 12 2022 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt4
- don't switch next video if not available (closes: 42407)

* Mon Apr 11 2022 Slava Aseev <ptrnine@altlinux.org> 0.7.3-alt3
- fix lags on time sync

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt2
- don't save playback position by default

* Thu Dec 23 2021 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt1
- initial build
