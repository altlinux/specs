%define rname kteatime

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Handy timer
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kteatime = %EVR
Obsoletes: kde5-kteatime < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kcolorscheme-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-sonnet-devel

%description
Handy timer for steeping tea.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kteatime
%_K6xdgapp/org.kde.kteatime.desktop
%_K6icon/*/*/apps/kteatime.*
%_K6notif/kteatime*
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

