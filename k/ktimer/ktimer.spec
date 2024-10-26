%define rname ktimer

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Application executor
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-ktimer = %EVR
Obsoletes: kde5-ktimer < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel

%description
Lets you start an application after a certain amount of time has passed.


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKF_IGNORE_PLATFORM_CHECK=ON \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/ktimer
%_K6xdgapp/org.kde.ktimer.desktop
%_K6icon/*/*/*/ktimer.*
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

