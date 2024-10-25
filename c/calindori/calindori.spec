%define rname calindori

%define sover 0
%define libcalindori libcalindori%sover

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Summary: Calendar application for Plasma Mobile
License: GPL-3.0-only
Group: Office
Url: https://anongit.kde.org/calindori.git

Requires: kf6-kirigami
Provides:  kde5-calindori = %EVR
Obsoletes: kde5-calindori < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-knotifications-devel
BuildRequires: kf6-kservice-devel kf6-kpeople-devel

%description
Calindori is a touch friendly calendar application. It has been designed for mobile devices but it can also run on desktop environments. It offers:
* Monthly agenda
* Multiple calendars
* Event management
* Task management
* Calendar import

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K6bin/calind*
%_K6xdgapp/*calind*.desktop
%_K6start/*calind*.desktop
%_K6icon/*/*/apps/*calind*.*
%_K6notif/*calind*.notifyrc
%_K6dbus_srv/*calind*.service
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

