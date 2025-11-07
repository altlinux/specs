%def_enable snapshot

%define xdg_name im.kaidan.kaidan

Name: kaidan
Version: 0.13.0
Release: alt1

Summary: Modern Chat App for Every Device
Group: Networking/Instant messaging
License: GPL-3.0-or-later
Url: https://kaidan.im

Vcs: https://invent.kde.org/network/kaidan.git

%if_disabled snapshot
#Source: https://invent.kde.org/network/-/archive/v%version/%name-v%version.tar.gz
Source: https://download.kde.org/unstable/kaidan/%version/%name-v%version.tar.xz
%else
Source: %name-v%version.tar
%endif

%K6init no_altplace appdata

%define qxmpp_ver 1.11.0
%define qt_ver 6.6
%define kf_ver 6.11
%define kr_ver 1.4.0

# KDE Dependencies Hell
Requires: qt6-svg kf6-kirigami-addons
Requires: libqt6-multimedia libqt6-multimediaquick
Requires: libkf6prisonscanner libqt6-location
Requires: libkf6sonnetui
Requires: kde6-kquickimageeditor
Requires: kf6-qqc2-desktop-style
#Requires: ...

BuildRequires(pre): rpm-build-kf6
BuildRequires: gcc-c++ extra-cmake-modules
BuildRequires: pkgconfig(QXmppQt6) >= %qxmpp_ver
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Positioning)
BuildRequires: pkgconfig(Qt6Location)
BuildRequires: pkgconfig(KF6WindowSystem) >= %kf_ver
BuildRequires: kf6-kio-devel
BuildRequires: kf6-prison-devel
BuildRequires: libkdsingleapplication-qt6-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kirigami-addons-devel >= %kr_ver
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-qqc2-desktop-style-devel
BuildRequires: libqtkeychain-qt6-devel

%description
Kaidan is a user-friendly and modern chat app for every device. It uses
the open communication protocol XMPP (Jabber). Unlike other chat apps,
you are not dependent on one specific service provider.

%prep
%setup -n %name-v%version

%build
%K6build
%install
%K6install
%K6find_qtlang %name --all-name

%files -f %name.lang
%_K6bin/%name
%_K6xdgapp/%xdg_name.desktop
%_K6icon/*/*/apps/%name.*
%_K6notif/%name.notifyrc
%_datadir/%name/
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/qlogging-categories6/kaidan.categories
%doc NEWS.md README.md

%changelog
* Fri Nov 07 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- v0.13.0-21-g7dc198a8

* Tue May 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- first build for Sisyphus (v0.12.2-14-g76578409)


