%define rname kweather

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Weather application
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami-addons
Provides: kde5-kweather = %EVR
Obsoletes: kde5-kweather < %EVR

Source: %rname-%version.tar
Patch1: alt-clear-country-names.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-charts-devel qt6-svg-devel qt6-declarative-devel
BuildRequires: kf6-ki18n-devel kf6-kirigami-devel kf6-kirigami-addons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kservice-devel
BuildRequires: kweathercore-devel
BuildRequires: plasma6-lib-devel

%description
A convergent weather application for Plasma.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kweather
%_K6plug/plasma/applets/*kweather*.so
%_K6xdgapp/*kweather*.desktop
%_K6dbus_srv/*kweather*.service
%_K6icon/hicolor/*/apps/*kweather*
%_K6data/plasma/plasmoids/*kweather*/
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

