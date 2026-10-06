%global optflags_lto %optflags_lto -ffat-lto-objects

%define rname plasma-dialer

Name: %rname
Version: 6.7.5
Release: alt1
%K6init

Group: Networking/Other
Summary: Phone dialer for Plasma Mobile
Url: https://invent.kde.org/plasma-mobile/plasma-dialer
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-only

Source: %rname-%version.tar

#Requires: ModemManager callaudiod
Requires: kf6-kirigami kf6-kirigami-addons

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-shadertools-devel qt6-multimedia-devel
BuildRequires: libphonenumber-devel
BuildRequires: libcallaudio-devel
BuildRequires: libwayland-client-devel wayland-devel
BuildRequires: kf6-kirigami-devel kf6-kirigami-addons-devel
BuildRequires: kf6-ki18n-devel kf6-kcontacts-devel kf6-kpeople-devel
BuildRequires: kf6-knotifications-devel kf6-kconfig-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-modemmanager-qt-devel
BuildRequires: kf6-kio-devel kf6-kwindowsystem-devel kf6-kcrash-devel
BuildRequires: plasma-wayland-protocols
#BuildRequires: KTactileFeedback

%description
Plasma Dialer is a phone application for Plasma Mobile. It provides
voice calls, a dial pad, contacts, call history and USSD support using
ModemManager and the KDE telephony services.

%package devel
Summary: Development files for KDE telephony
Group: Development/KDE and QT

%description devel
This package contains KDE telephony D-Bus interface descriptions,
metatype headers and the static metatype library.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DMODEM_SUBSYSTEM=ModemManager \
    #
#    -DDIALER_BUILD_SHELL_OVERLAY=ON \

%install
%K6install
%find_lang --with-kde --all-name %name

%files -f %name.lang
%doc README.md LICENSES/*
%_K6bin/plasma-dialer
%_K6libexecdir/modem-daemon
%_K6libexecdir/kde-telephony-daemon
%_K6qml/org/kde/telephony/
%_K6dbus_srv/org.kde.modemdaemon.service
%_K6dbus_srv/org.kde.telephony.service
%_K6start/*daemon*.desktop
%_K6xdgapp/*dialer*.desktop
%_K6icon/hicolor/*/apps/*dialer*
%_K6notif/*dialer*
%_datadir/metainfo/*dialer*

%files devel
%_K6bin/plasma-dialer-fakeserver
%_K6inc/kTelephonyMetaTypes/
%_K6lib/libktelephonymetatypes.a
%_K6dbus_iface/*telephony*.xml

%changelog
* Tue Oct 06 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.5-alt1
- initial build
