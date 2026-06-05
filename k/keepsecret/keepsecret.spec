%define rname keepsecret

Name: %rname
Version: 1.1.0
Release: alt2
%K6init

Summary: Password manager GUI for KDE Plasma
Group: Graphical desktop/KDE
License: GPL-2.0
Url: https://invent.kde.org/utilities/keepsecret

Requires: kf6-kirigami kf6-kirigami-addons

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-quick3d-devel qt6-svg-devel qt6-virtualkeyboard-devel qt6-wayland-devel
BuildRequires: qt6-virtualkeyboard
#BuildRequires: qt6-webengine-devel
BuildRequires: libsecret-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kirigami kf6-kirigami-devel kf6-kitemmodels-devel

%description
KeepSecret is a Password manager GUI intended to be a client for
a Secret Service compatible provider.

It can be used with KWallet, but also other systems such as oo7, Gnome-keyring or KeepassXC.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang --with-kde %rname

%files -f %rname.lang
%_K6bin/%rname
%_K6xdgapp/*keepsecret*.desktop
%_K6icon/*/*/apps/*keepsecret*.*
%_datadir/metainfo/*keepsecret*.xml
%_datadir/qlogging-categories6/*keepsecret*

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- add russian translation

* Wed Jun 03 2026 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- initial build
