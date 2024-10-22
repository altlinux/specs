%define rname audiotube

%define sover 6
%define libaudiotubecore libaudiotubecore%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Sound
Summary: YouTube Music client
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt6-multimedia qt6-imageformats
Requires: python3(ytmusicapi) python3(yt_dlp)
Requires: kf6-kirigami-addons
Provides: kde5-audiotube = %EVR
Obsoletes: kde5-audiotube < %EVR

Source: %rname-%version.tar
Patch1: alt-buildreq.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: pybind11-devel python3-devel python3(ytmusicapi) python3(yt_dlp)
BuildRequires: qt6-declarative-devel qt6-multimedia-devel qt6-svg-devel
BuildRequires: futuresql-qt6-devel qcoro6-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-ki18n-devel kf6-kirigami-addons-devel
BuildRequires: kf6-kirigami-devel kf6-kwindowsystem-devel

%description
Convergent YouTube Music client.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6xdgapp/*audiotube.desktop
%_K6icon/*/*/apps/*%{rname}*
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

