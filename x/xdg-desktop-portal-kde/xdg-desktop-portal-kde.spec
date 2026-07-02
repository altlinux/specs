%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname xdg-desktop-portal-kde
Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE6 xdg-desktop-portal
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-xdg-desktop-portal-kde = %EVR
Obsoletes: plasma5-xdg-desktop-portal-kde < %EVR

Requires: xdg-desktop-portal
Requires: libkf6iconthemes
Requires: plasma-workspace-qml
#Requires: kio-fuse

Source: %rname-%version.tar
Source1: env.sh
Patch1: alt-xdg-current-desktop.patch

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
%patch1 -p1

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
#%_datadir/xdg-desktop-portal/*kde*.conf
%config(noreplace) %_K6xdgconf/plasma-workspace/env/*.sh
%_userunitdir/*.service
%_datadir/qlogging-categories6/*.*categories



%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Mon Apr 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt2
- fix parsing $XDG_CURRENT_DESKTOP (closes: 53733)

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Fri Sep 20 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt2
- don't export GTK_USE_PORTAL=1 because GTK3 fonts antialiasing fail

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

