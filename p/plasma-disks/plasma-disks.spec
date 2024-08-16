%define rname plasma-disks

Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma Hard disk health monitoring
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: /usr/sbin/smartctl

Provides: plasma5-disks = %EVR
Obsoletes: plasma5-disks < %EVR

Source: %rname-%version.tar
Patch1: alt-utilbuttons.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: qt6-base-devel
BuildRequires: extra-cmake-modules kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-kded kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kcmutils-devel
%description
Monitors S.M.A.R.T. capable devices for imminent failure.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6dbus_sys_srv/*smart*.service
%_K6plug/plasma/kcms/kinfocenter/*disks*.so
%_K6plug/kf6/kded/smart.so
%_K6exec/kauth/*smart*
%_K6notif/*smart*.notifyrc
%_K6xdgapp/*disks*.desktop
%_K6dbus/system.d/*smart*.conf
%_datadir/polkit-1/actions/*smart*.policy
%_datadir/metainfo/*.xml

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

