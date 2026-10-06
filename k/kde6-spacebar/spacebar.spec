%define rname spacebar

Name: kde6-%rname
Version: 6.7.5
Release: alt1
%K6init

Group: Networking/Instant messaging
Summary: SMS and MMS application for Plasma Mobile
Url: https://invent.kde.org/plasma-mobile/spacebar
License: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL

Source: %rname-%version.tar

#Requires: ModemManager
Requires: kf6-kirigami kf6-kirigami-addons

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-shadertools-devel
BuildRequires: kf6-kirigami-devel kf6-kirigami-addons-devel
BuildRequires: kf6-ki18n-devel kf6-kcontacts-devel kf6-kpeople-devel
BuildRequires: kf6-knotifications-devel kf6-kconfig-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-modemmanager-qt-devel
BuildRequires: kf6-kio-devel kf6-kwindowsystem-devel kf6-kcrash-devel
BuildRequires: libphonenumber-devel libcurl-devel libcares-devel
BuildRequires: libvulkan-devel
BuildRequires: futuresql-qt6-devel qcoro6-devel

%description
Spacebar is an SMS and MMS messaging application for Plasma Mobile.
It uses ModemManager to send and receive messages over mobile networks.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang --with-kde --all-name %name

%files -f %name.lang
%doc README.md LICENSES/*
%_K6bin/spacebar
%_K6libexecdir/spacebar-daemon
%_K6start/*spacebar*.desktop
%_K6xdgapp/*spacebar*.desktop
%_K6icon/hicolor/*/apps/*spacebar*
%_datadir/metainfo/*spacebar*
%_K6notif/*spacebar*

#%files devel
#%_K6bin/spacebar-fakeserver

%changelog
* Tue Oct 06 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.5-alt1
- initial build
