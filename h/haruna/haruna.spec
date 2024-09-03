%define rname haruna

%define sover 0
%define libharuna libharuna%sover

Name: %rname
Version: 1.2.0
Release: alt1
%K6init

Group: Video
Summary: Video Player
Url: https://invent.kde.org/multimedia/haruna
License: GPL-3.0-or-later

Requires: %name-youtube-player
Provides: kde5-haruna = %EVR
Obsoletes: kde5-haruna < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-5compat-devel
BuildRequires: mpvqt6-devel
BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libavfilter-devel libswscale-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kdoctools-devel kf6-kfilemetadata-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kirigami-devel kf6-kxmlgui-devel
BuildRequires: plasma6-breeze-devel

%description
Haruna is an open source video player built with Qt/QML and libmpv.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-haruna-common = %EVR
Obsoletes: kde5-haruna-common < %EVR
%description common
%name common package

%package -n %name-youtube-player-4-ytdlp
Group: System/Configuration/Other
Summary: %name youtube player
Provides: %name-youtube-player
Provides: %name-youtube-player-ytdlp
Requires: %name-common
Provides: kde5-haruna-youtube-player-4-ytdlp = %EVR
Obsoletes: kde5-haruna-youtube-player-4-ytdlp < %EVR
Requires: yt-dlp
%description -n %name-youtube-player-4-ytdlp
%name youtube player.

%package -n %name-youtube-player-2-youtubedl
Group: System/Configuration/Other
Summary: %name youtube player
Provides: %name-youtube-player
Provides: %name-youtube-player-youtubedl
Requires: %name-common
Provides: kde5-haruna-youtube-player-2-youtubedl = %EVR
Obsoletes: kde5-haruna-youtube-player-2-youtubedl < %EVR
Requires: youtube-dl
%description -n %name-youtube-player-2-youtubedl
%name youtube player.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kde5-haruna-devel = %EVR
Obsoletes: kde5-haruna-devel < %EVR
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libharuna
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libharuna
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K6install
%K6install_move data locale
%find_lang %name --with-kde --all-name

%files common
%doc LICENSES/*
%files -n %name-youtube-player-4-ytdlp
%files -n %name-youtube-player-2-youtubedl
%files -f %name.lang
%doc README.md
%_K6bin/haruna
%_K6xdgapp/*haruna*.desktop
%_K6icon/hicolor/*/apps/*haruna*.*
%_datadir/metainfo/*haruna*.xml

#%files -n %libharuna
#%doc LICENSE* README.md
#%_K6lib/libharuna.so.%sover
#%_K6lib/libharuna.so.*

%changelog
* Tue Sep 03 2024 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- initial build
