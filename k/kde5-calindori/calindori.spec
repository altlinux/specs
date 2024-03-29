%define rname calindori

%define sover 0
%define libcalindori libcalindori%sover

Name: kde5-%rname
Version: 23.08.5
Release: alt1
%K5init

Summary: Calendar application for Plasma Mobile
License: GPL-3.0-only
Group: Office
Url: https://anongit.kde.org/calindori.git

Requires: kf5-kirigami

Source: %rname-%version.tar
Patch1: fix-segfault-when-deleting-event-or-todo.patch

# Automatically added by buildreq on Thu Mar 19 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-devel libdb4-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kf5-kcalcore-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kservice-devel libssl-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kcalcore-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel
BuildRequires: kf5-kservice-devel kf5-kpeople-devel

%description
Calindori is a touch friendly calendar application. It has been designed for mobile devices but it can also run on desktop environments. It offers:
* Monthly agenda
* Multiple calendars
* Event management
* Task management
* Calendar import

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K5bin/calind*
%_K5xdgapp/*calind*.desktop
%_K5start/*calind*.desktop
%_K5icon/*/*/apps/*calind*.*
%_K5notif/*calind*.notifyrc
%_K5dbus_srv/*calind*.service
%_datadir/metainfo/*.xml

%changelog
* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Dec 18 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt2
- fix segfault when deleting event or todo from associated lists (closes: 42708) (thanks krf10@alt)

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Wed Jun 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 23.01.0-alt1
- new version

* Mon Dec 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.11-alt1
- new version

* Wed Oct 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.09-alt1
- new version

* Tue Jul 05 2022 Sergey V Turchin <zerg@altlinux.org> 22.06-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 22.04-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 22.02-alt1
- new version

* Fri Dec 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.12-alt1
- new version

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08-alt1
- new version

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- new version

* Thu Mar 19 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
