%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname xdg-desktop-portal-kde
Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE6 xdg-desktop-portal
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-xdg-desktop-portal-kde = %EVR
Obsoletes: plasma5-xdg-desktop-portal-kde < %EVR

Requires: xdg-desktop-portal
Requires: plasma-workspace-qml
#Requires: kio-fuse

Source: %rname-%version.tar
Source1: env.sh

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: qt6-wayland-devel qt6-base-devel
BuildRequires: libcups-devel glib2-devel libepoxy-devel libgbm-devel libssl-devel pipewire-libs-devel
BuildRequires: extra-cmake-modules kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-kirigami-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kiconthemes-devel kf6-kstatusnotifieritem-devel
# python3-dev
BuildRequires: wayland-protocols plasma-wayland-protocols
BuildRequires: plasma6-kwayland-devel


%description
A backend implementation for [xdg-desktop-portal](http://github.com/flatpak/xdg-desktop-portal)
that is using Qt/KF6.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data xdg-desktop-portal-kde
mkdir -p %buildroot/%_K6xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K6xdgconf/plasma-workspace/env/%{name}.sh
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6xdgapp/*portal*kde*.desktop
%_K6libexecdir/*portal*kde*
%_K6dbus_srv/*portal*kde*.service
%_K6notif/*portal*kde*.notifyrc
%_datadir/xdg-desktop-portal/portals/kde.portal
%_datadir/xdg-desktop-portal/*kde*.conf
%config(noreplace) %_K6xdgconf/plasma-workspace/env/*.sh
%_userunitdir/*.service
%_datadir/qlogging-categories6/*.*categories



%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

