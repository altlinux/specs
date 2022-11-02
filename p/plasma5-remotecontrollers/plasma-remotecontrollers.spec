%define rname plasma-remotecontrollers

Name: plasma5-remotecontrollers
Version: 5.26.2
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: Input events to keypresses translator
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common
Requires: qml(org.kde.plasma.core)

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Nov 02 2022 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kjobwidgets-common kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-plasma-framework-common kf5-solid-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libcec-platform-devel libctf-nobfd0 libdbusmenu-qt52 libfreetype-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-sql libqt5-svg libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 shared-mime-info tzdata wayland-devel xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream extra-cmake-modules icon-theme-breeze kde5-plasma-wayland-protocols kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kitemmodels-devel kf5-knotifications-devel kf5-kpackage-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcec-devel libevdev-devel libkf5plasmaquick libqtxdg libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel lua5.3 plasma5-workspace-devel python-modules-compiler python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-translations qt5-wayland-devel rpm-build-qml6 tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules rpm-build-qml
BuildRequires: libcec-devel libevdev-devel
BuildRequires: kde5-plasma-wayland-protocols qt5-wayland-devel
BuildRequires: kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kitemmodels-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel
BuildRequires: plasma5-workspace-devel

%description
This project translates events from various input devices to keypresses
on a keyboard and pointer events (mouse movement).

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

%package -n libplasma-remotecontrollers
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-remotecontrollers
%name library

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data locale kpackage
# fix install autostart
mkdir -p %buildroot/%_K5start/
mv %buildroot/%_sysconfdir/xdg/autostart/*.desktop \
    %buildroot/%_K5start/
# rename udev rules
mkdir -p %buildroot/%_udevrulesdir/
mv %buildroot/%_libdir/udev/rules.d/40-uinput.rules %buildroot/%_udevrulesdir/40-uinput-%name.rules

%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_udevrulesdir/*.rules
%config(noreplace) %_K5xdgconf/plasma-remotecontrollersrc
%_K5bin/*remotecontrollers*
%_K5plug/kcms/*remotecontrollers*.so
%_K5qml/org/kde/plasma/remotecontrollers/
%_K5start/org.kde.plasma-remotecontrollers.desktop
%_K5xdgapp/*remotecontrollers*.desktop
%_K5data/kpackage/kcms/kcm_mediacenter_remotecontrollers/
%_K5notif/*remotecontrollers*
%_K5srv/*remotecontrollers*.desktop
%_datadir/qlogging-categories5/*.*categories

%files devel
%_K5dbus_iface/*remotecontrollers*

%changelog
* Tue Nov 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- initial build
