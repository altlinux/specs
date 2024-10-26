%define rname dragon

Name: %{rname}player
Version: 24.08.2
Release: alt1
%K6init

Group: Video
Summary: Video Player for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-dragon = %EVR
Obsoletes: kde5-dragon < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: qt6-phonon-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kcrash-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data solid doc
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6xdgconf/*rc
%_K6bin/*
%_K6plug/kf6/parts/*.so
%_K6xdgapp/*.desktop
%_K6icon/*/*/apps/*.*
%_K6icon/*/*/actions/player-*.*
%_K6data/kio/servicemenus/*dragon*.desktop
%_K6data/solid/actions/*.desktop
%_datadir/metainfo/*.xml

%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

