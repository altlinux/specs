%define rname ffmpegthumbs

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Video
Summary: Video thumbnail generator
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-ffmpegthumbs = %EVR
Obsoletes: kde5-ffmpegthumbs < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libavcodec-devel libavutil-devel libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel libavfilter-devel
BuildRequires: libtag-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-ki18n-devel

%description
Video thumbnail generator for KDE.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6cfg/ffmpegthumb*.kcfg
%_K6plug/kf6/thumbcreator/ffmpegthumbs.so
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

