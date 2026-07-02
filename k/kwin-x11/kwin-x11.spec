%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kwin-x11

%define kwin_sover 6
%define libkwin libkwin-x11_%kwin_sover
%define kcmkwincommon_sover 6
%define libkcmkwincommon libkcmkwincommon-x11_%kcmkwincommon_sover
%define kwineffects_sover 14
%define libkwineffects libkwineffects%kwineffects_sover
%define kwinglutils_sover 14
%define libkwinglutils libkwinglutils%kwinglutils_sover
%define kwinxrenderutils_sover 14
%define libkwinxrenderutils libkwinxrenderutils%kwinxrenderutils_sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Window Manager
Url: http://www.kde.org
License: GPL-2.0-or-later

Conflicts: kwin < 6.4

Requires: hwdata
Requires: qt6-multimedia qt6-virtualkeyboard qt6-declarative
Requires: kf6-kirigami kscreenlocker kf6-kdeclarative
Requires: kwin-aurorae
Requires(post): /sbin/setcap

Source: %rname-%version.tar
#
Patch1: alt-def-window-buttons.patch
Patch2: alt-def-layout-switch.patch
Patch3: alt-def-tiling-layout.patch
Patch4: alt-def-numlock.patch
Patch5: alt-xdg-current-desktop.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel qt6-5compat-devel
BuildRequires: libqaccessibilityclient-qt6-devel
BuildRequires: libcanberra-devel
BuildRequires: libcap-utils libcap-devel zlib-devel
BuildRequires: libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-cursor-devel libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel libgbm-devel libdrm-devel libEGL-devel libxcvt-devel libXi-devel
BuildRequires: fontconfig-devel libfreetype-devel liblcms2-devel
BuildRequires: libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: pipewire-libs-devel
BuildRequires: hwdata-devel
BuildRequires: pkgconfig(libdisplay-info) pkgconfig(libeis-1.0)
BuildRequires: libvulkan-devel
BuildRequires: libsystemd-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols wayland-protocols
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-tools-devel-static  qt6-sensors-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel  kf6-solid-devel kf6-sonnet-devel kf6-kidletime-devel
BuildRequires: kf6-kirigami-devel kf6-krunner-devel kf6-kglobalaccel-devel kf6-ksvg-devel
BuildRequires: kscreenlocker-devel plasma6-breeze-devel plasma6-kdecoration-devel plasma6-activities-devel
BuildRequires: plasma6-kglobalacceld-devel plasma6-kwayland-devel knighttime-devel

%description
KDE Window Manager

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libdrm-devel
Conflicts: plasma5-kwin-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwin
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkwin
KF6 library

%package -n %libkcmkwincommon
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkcmkwincommon
KF6 library

%package -n %libkwineffects
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkwineffects
KF6 library

%package -n %libkwinglutils
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkwinglutils
KF6 library

%package -n %libkwinxrenderutils
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkwinxrenderutils
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

for f in src/kcms/compositing/kwincompositing.json ; do
    sed -i '/X-DocPath/d' $f
done

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kconf_update knsrcfiles krunner
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/*/*/apps/*.*

%files
%_datadir/qlogging-categories6/*.*categories
%_K6bin/kwin*
%_K6libexecdir/*kwin*
%_K6plug/kf6/packagestructure/kwin_*.so
%_K6plug/kwin-x11/
%_K6plug/plasma/kcms/systemsettings/*kwin*.so
%_K6plug/plasma/kcms/systemsettings/*animations*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/*kwin*.so
%_K6xdgapp/*kwin*.desktop
%_K6xdgapp/*animations*.desktop
%_K6cf_bin/kwin*
%_K6conf_up/kwin*
%_K6qml/org/kde/kwin*/
%_K6data/kwin-x11/
%_K6data/knsrcfiles/*.knsrc
%_K6data/krunner/dbusplugins/*.desktop
%_K6notif/*.notifyrc
%_userunitdir/*.service

%files devel
%_K6inc/kwin-x11/
%_K6link/lib*.so
%_K6lib/cmake/KWin*/
%_K6dbus_iface/*.xml

%files -n %libkwin
%_K6lib/libkwin-x11.so.%kwin_sover
%_K6lib/libkwin-x11.so.*
%files -n %libkcmkwincommon
%_K6lib/libkcmkwincommon-x11.so.%kcmkwincommon_sover
%_K6lib/libkcmkwincommon-x11.so.*

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

* Mon Mar 23 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt2
- cleanup from wayland

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Mon Dec 01 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt2
- fix parse $XDG_CURRENT_DESKTOP

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

* Thu Jul 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt2
- fix requires

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- initial build
