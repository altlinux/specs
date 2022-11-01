%define rname plasma-disks

Name: plasma5-disks
Version: 5.26.2
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 Hard disk health monitoring
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: /usr/sbin/smartctl

Source: %rname-%version.tar
Patch1: alt-utilbuttons.patch

# Automatically added by buildreq on Fri Dec 04 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libctf-nobfd0 libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kded kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kpackage-devel libkf5kcmutils python-modules-compiler python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel smartmontools
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: extra-cmake-modules kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kded kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel
%description
Monitors S.M.A.R.T. capable devices for imminent failure.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-disks
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-disks
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5dbus_sys_srv/*smart*.service
%_K5plug/plasma/kcms/kinfocenter/*smart*.so
%_K5plug/kf5/kded/smart.so
%_K5libexecdir/kauth/*smart*
%_K5notif/*smart*.notifyrc
%_K5data/kpackage/kcms/plasma_disks/
%_K5dbus/system.d/*smart*.conf
%_datadir/polkit-1/actions/*smart*.policy

%changelog
* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 5.21.3-alt1
- new version

* Thu Jan 21 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt2
- add gparted button

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.20.5-alt1
- new version

* Fri Dec 04 2020 Sergey V Turchin <zerg@altlinux.org> 5.20.4-alt1
- initial build
