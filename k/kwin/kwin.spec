%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kwin

%define kwin_sover 6
%define libkwin libkwin%kwin_sover
%define kcmkwincommon_sover 6
%define libkcmkwincommon libkcmkwincommon%kcmkwincommon_sover
%define kwineffects_sover 14
%define libkwineffects libkwineffects%kwineffects_sover
%define kwinglutils_sover 14
%define libkwinglutils libkwinglutils%kwinglutils_sover
%define kwinxrenderutils_sover 14
%define libkwinxrenderutils libkwinxrenderutils%kwinxrenderutils_sover

Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Window Manager
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kwin = %EVR
Obsoletes: plasma5-kwin < %EVR

Requires: hwdata
Requires: /usr/bin/Xwayland
Requires: qt6-multimedia qt6-virtualkeyboard qt6-declarative
Requires: kf6-kirigami kscreenlocker kf6-kdeclarative
Requires: libplasmaquick6
Requires(post): /sbin/setcap

Source: %rname-%version.tar
#
Patch1: alt-def-window-buttons.patch
Patch2: alt-def-layout-switch.patch

BuildRequires(pre): rpm-build-kf6 libwayland-client-devel
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel qt6-5compat-devel
BuildRequires: libqaccessibilityclient-qt6-devel
BuildRequires: libcap-utils libcap-devel zlib-devel
BuildRequires: libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-cursor-devel libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel libgbm-devel libdrm-devel libEGL-devel libxcvt-devel
BuildRequires: fontconfig-devel libfreetype-devel liblcms2-devel
BuildRequires: libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: pipewire-libs-devel
BuildRequires: hwdata-devel
BuildRequires: pkgconfig(libdisplay-info) pkgconfig(libeis-1.0)
BuildRequires: libvulkan-devel
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
BuildRequires: plasma6-kglobalacceld-devel plasma6-kwayland-devel

%description
KDE Window Manager

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-kwin-common = %EVR
Obsoletes: plasma5-kwin-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-kwin-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwin
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Requires: libwayland-client = %{get_version libwayland-client-devel}
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

%post
/sbin/setcap CAP_SYS_NICE=+ep %_K6bin/kwin_wayland ||:

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/*/*/apps/*.*

%files
%_datadir/qlogging-categories6/*.*categories
%_K6bin/kwin*
%_K6libexecdir/*kwin*
%_K6plug/kf6/packagestructure/kwin_*.so
%_K6plug/org.kde.kdecoration2.kcm/
%_K6plug/plasma/kcms/systemsettings/*keyboard*.so
%_K6plug/kwin/
%_K6plug/plasma/kcms/systemsettings/*kwin*.so
%_K6plug/plasma/kcms/systemsettings_qwidgets/*kwin*.so
%_K6plug/org.kde.kdecoration2/
%_K6xdgapp/*kwin*.desktop
%_K6xdgapp/*keyboard*.desktop
%_K6cf_bin/kwin*
%_K6conf_up/kwin*
%_K6qml/org/kde/kwin*/
%_K6cfg/*.kcfg
%_K6data/kwin/
%_K6data/knsrcfiles/*.knsrc
%_K6data/krunner/dbusplugins/*.desktop
%_K6notif/*.notifyrc
%_userunitdir/*.service

%files devel
%_K6inc/kwin/
%_K6link/lib*.so
%_K6lib/cmake/KWin*/
%_K6dbus_iface/*.xml

#%files -n %libkwineffects
#%_K6lib/libkwineffects.so.%kwineffects_sover
#%_K6lib/libkwineffects.so.*
#%files -n %libkwinglutils
#%_K6lib/libkwingl*utils.so.%kwinglutils_sover
#%_K6lib/libkwingl*utils.so.*
%files -n %libkwin
%_K6lib/libkwin.so.%kwin_sover
%_K6lib/libkwin.so.*
%files -n %libkcmkwincommon
%_K6lib/libkcmkwincommon.so.%kcmkwincommon_sover
%_K6lib/libkcmkwincommon.so.*

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

